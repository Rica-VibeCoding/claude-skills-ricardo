#!/usr/bin/env python3
"""
Promob Text Parser - Efficient structured data processing
Handles 90% of the work with code, uses AI only for decisions
"""

import re
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass, field


@dataclass
class PromobData:
    """Stores parsed and categorized Promob data"""
    caixa: Dict[str, Set[str]] = field(default_factory=dict)
    portas_frentes: Dict[str, Set[str]] = field(default_factory=dict)
    puxadores: Dict[str, Set[str]] = field(default_factory=dict)
    porta_vidro: Dict[str, Set[str]] = field(default_factory=dict)
    ferragens: Dict[str, Set[str]] = field(default_factory=dict)
    paineis: Dict[str, Set[str]] = field(default_factory=dict)
    vidros: Set[str] = field(default_factory=set)
    componentes: Dict[str, Set[str]] = field(default_factory=dict)
    estrutura: Dict[str, Set[str]] = field(default_factory=dict)
    serralheria: Dict[str, Set[str]] = field(default_factory=dict)
    iluminacao: Dict[str, Set[str]] = field(default_factory=dict)
    acessorios: Dict[str, Set[str]] = field(default_factory=dict)
    portas_passagem: Dict[str, Set[str]] = field(default_factory=dict)
    unknown_items: List[Tuple[str, str]] = field(default_factory=list)  # (field, value)


class PromobParser:
    """Fast parser for structured Promob text"""

    # Sections to completely ignore
    IGNORE_SECTIONS = {'Decore', 'Componentes Avulsos', 'Montagem'}

    # Fields to always skip
    IGNORE_FIELDS = {
        'Fita de Borda', 'Fita Caixas', 'Fita de Borda Portas/Frentes',
        'Fita Frontal', 'Fita Prateleira', 'Fita Corpos de Gaveta',
        'Fita de Borda Tampo', 'Fita de Borda Ld Externo', 'Fita de Borda Ld Interno',
        'Fita de Borda Frentes Internas', 'Fita Ripas',
        'Tipo de Fundo', 'Tipo de Fundo Despenseiro', 'Tipo de Fundo Superiores',
        'Tipo de Fundo Armários de Canto', 'Tipo Fundo Inferior',
        'Modelo s/ Rodapé', 'Gaveta Externa'
    }

    # Environment titles to skip
    IGNORE_ENVIRONMENTS = {
        'Cozinhas', 'Dormitórios', 'Sala', 'Banheiros', 'Lavanderia',
        'Escritório', 'FGVTN'
    }

    # Field to category mapping
    FIELD_MAPPING = {
        # CAIXA
        'Caixas': ('caixa', 'Cores'),
        'Corpo de Gavetas': ('caixa', 'Corpo de Gavetas'),
        'Frente Gaveta Interna': ('caixa', 'Frente Gaveta Interna'),
        'Frente de Gaveta Criado': ('caixa', 'Frente de Gaveta Criado'),
        'Base Estrutural': ('caixa', 'Base Estrutural'),
        'Modelo Interno Canto L': ('caixa', 'Modelo Interno Canto L'),
        'Modelo Interno': ('caixa', 'Modelo Interno'),

        # PORTAS / FRENTES
        'Portas': ('portas_frentes', 'Tipos'),
        'Acab. Portas/Frentes': ('portas_frentes', 'Acabamentos'),
        'Acab. Frentes Internas': ('portas_frentes', 'Frentes Internas'),
        'Miolo Porta': ('portas_frentes', 'Miolo Porta'),
        'Basculantes': ('portas_frentes', 'Tipos'),

        # PUXADORES
        'Puxador Perfil': ('puxadores', 'main'),
        'Puxador Perfil Rometal': ('puxadores', 'main'),
        'Acab Puxador': ('puxadores', 'Acabamento Puxador'),
        'Puxador Externo': ('puxadores', 'main'),
        'Acab Pux Externo': ('puxadores', 'Acabamento Puxador'),
        'Puxador Interno': ('puxadores', 'main'),
        'Acab Pux Interno': ('puxadores', 'Acabamento Puxador'),
        'Puxadores Metálicos': ('puxadores', 'Obispa'),
        'Puxadores': ('puxadores', 'Obispa'),

        # PORTA DE VIDRO
        'Porta Perfil': ('porta_vidro', 'Porta Perfil'),
        'Perfil Rometal': ('porta_vidro', 'Perfil Rometal'),
        'Puxador': ('porta_vidro', 'Puxador'),
        'Vidros': ('vidros', None),

        # FERRAGENS
        'Dobradiça': ('ferragens', 'Dobradiça'),
        'Fechadura': ('ferragens', 'Fechadura'),

        # PAINÉIS
        'Painéis': ('paineis', 'main'),
        'Tampos': ('paineis', 'main'),
        'Ripas': ('paineis', 'Ripas'),

        # ACESSÓRIOS
        'Cabideiro': ('acessorios', 'Cabideiro'),
        'Cabideiro Vesto': ('acessorios', 'Cabideiro'),
        'Alternativa': ('acessorios', 'Alternativa'),

        # SERRALHERIA
        'Metalon': ('serralheria', 'Metalon'),

        # PORTAS DE PASSAGEM
        'Acab. Interno': ('portas_passagem', 'Acabamento Interno'),
        'Acab. Externo': ('portas_passagem', 'Acabamento Externo'),
    }

    def __init__(self):
        self.data = PromobData()

    def parse(self, text: str) -> PromobData:
        """Main parsing function"""
        current_section = None
        ignore_section = False

        for line in text.strip().split('\n'):
            line = line.strip()
            if not line:
                continue

            # Check if it's a section header (no leading dash)
            if not line.startswith('-'):
                section = line
                # Mark if we should ignore this section completely
                if section in self.IGNORE_SECTIONS:
                    ignore_section = True
                    continue
                # Environment sections: ignore title but process fields
                if section in self.IGNORE_ENVIRONMENTS:
                    ignore_section = False  # Process fields within
                    continue
                current_section = section
                ignore_section = False
                continue

            # Parse field: value format
            if not ignore_section and line.startswith('-'):
                self._parse_field(line[1:].strip())

        return self.data

    def _parse_field(self, field_line: str):
        """Parse a field line: 'Field: Value1, Value2'"""
        if ':' not in field_line:
            return

        field, values_str = field_line.split(':', 1)
        field = field.strip()

        # Skip ignored fields
        if field in self.IGNORE_FIELDS:
            return

        # Skip empty values
        values_str = values_str.strip()
        if not values_str:
            return

        # Split multiple values
        values = [v.strip() for v in values_str.split(',')]

        # Map field to category
        if field in self.FIELD_MAPPING:
            category, subcategory = self.FIELD_MAPPING[field]
            for value in values:
                cleaned_value = self._clean_value(value, field)
                if cleaned_value:
                    self._add_to_category(category, subcategory, cleaned_value)
        else:
            # Unknown field - store for AI decision
            for value in values:
                self.data.unknown_items.append((field, value))

    def _clean_value(self, value: str, field: str) -> str:
        """Clean and format values"""
        # Remove "MDF\" or "Alumínio\" prefixes from Portas field
        if field == 'Portas':
            value = re.sub(r'^(MDF|Alumínio|Aluminio)\\', '', value)

        # Convert "Marca Cor>Nome" to "MDF Marca Nome"
        if '>' in value:
            parts = value.split('>')
            if len(parts) == 2:
                prefix = parts[0].strip()
                name = parts[1].strip()

                # Handle special cases
                if prefix == 'MDF Cores':
                    return f'MDF {name}'
                elif 'Cor' in prefix or 'Madeirado' in prefix:
                    # Extract brand: "Duratex Cor", "Arauco Madeirado"
                    brand = prefix.replace(' Cor', '').replace(' Madeirado', '').strip()
                    return f'MDF {brand} {name}'

        # Handle path-like values (Wood Pro +\...)
        if '\\' in value and 'Wood Pro' in value:
            # Extract the last meaningful part
            parts = value.split('\\')
            return parts[-1].strip()

        # Replace backslashes with spaces (cleanup formatting)
        value = value.replace('\\', ' ')

        return value.strip()

    def _add_to_category(self, category: str, subcategory: str, value: str):
        """Add value to the appropriate category"""
        category_data = getattr(self.data, category)

        if category == 'vidros':
            category_data.add(value)
        else:
            if subcategory == 'main':
                subcategory = 'items'
            if subcategory not in category_data:
                category_data[subcategory] = set()
            category_data[subcategory].add(value)

    def format_output(self, include_dobradica: List[str] = None,
                     include_corredica: List[str] = None) -> str:
        """Format parsed data into clean output"""
        output = []

        # Helper to add section
        def add_section(title: str, data: Dict[str, Set[str]], order: List[str] = None):
            if not data:
                return

            output.append(f"\n\n{title}\n")

            # Determine order
            if order:
                keys = [k for k in order if k in data]
                keys += [k for k in data.keys() if k not in order]
            else:
                keys = sorted(data.keys())

            for key in keys:
                values = sorted(data[key])
                if key == 'items':
                    # No subcategory label
                    for v in values:
                        output.append(v)
                else:
                    output.append(f"\n{key}:")
                    for v in values:
                        output.append(v)

        # CAIXA
        add_section("CAIXA", self.data.caixa,
                   ['Cores', 'Base Estrutural', 'Corpo de Gavetas'])

        # PORTAS / FRENTES
        add_section("PORTAS / FRENTES", self.data.portas_frentes,
                   ['Tipos', 'Acabamentos', 'Frentes Internas', 'Miolo Porta'])

        # PUXADORES
        add_section("PUXADORES", self.data.puxadores,
                   ['items', 'Acabamento Puxador', 'Obispa'])

        # PORTA DE VIDRO
        if self.data.porta_vidro or self.data.vidros:
            output.append("\n\nPORTA DE VIDRO\n")
            if self.data.porta_vidro:
                for key in ['Porta Perfil', 'Perfil Rometal', 'Puxador']:
                    if key in self.data.porta_vidro:
                        output.append(f"\n{key}:")
                        for v in sorted(self.data.porta_vidro[key]):
                            output.append(v)
            if self.data.vidros:
                output.append("\nVidros:")
                for v in sorted(self.data.vidros):
                    output.append(v)

        # FERRAGENS
        if self.data.ferragens or include_dobradica or include_corredica:
            output.append("\n\nFERRAGENS\n")

            # Dobradiça
            if include_dobradica:
                output.append("\nDobradiça:")
                for d in include_dobradica:
                    output.append(d)
            elif 'Dobradiça' in self.data.ferragens:
                output.append("\nDobradiça:")
                for v in sorted(self.data.ferragens['Dobradiça']):
                    output.append(v)

            # Corrediça
            if include_corredica:
                output.append("\nCorrediça:")
                for c in include_corredica:
                    output.append(c)

            # Other hardware
            for key in self.data.ferragens:
                if key != 'Dobradiça':
                    output.append(f"\n{key}:")
                    for v in sorted(self.data.ferragens[key]):
                        output.append(v)

        # PAINÉIS / TAMPOS / TAMPONAMENTOS
        if self.data.paineis:
            output.append("\n\nPAINÉIS / TAMPOS / TAMPONAMENTOS\n")
            if 'items' in self.data.paineis:
                for v in sorted(self.data.paineis['items']):
                    output.append(v)
            if 'Ripas' in self.data.paineis:
                output.append("\nRipas:")
                for v in sorted(self.data.paineis['Ripas']):
                    output.append(v)

        # ACESSÓRIOS
        add_section("ACESSÓRIOS", self.data.acessorios)

        # SERRALHERIA
        add_section("SERRALHERIA", self.data.serralheria)

        # PORTAS DE PASSAGEM
        add_section("PORTAS DE PASSAGEM", self.data.portas_passagem,
                   ['Acabamento Interno', 'Acabamento Externo', 'Puxador Externo', 'Puxador Interno'])

        # Remove leading newlines
        result = '\n'.join(output).strip()
        return result


def main():
    """CLI interface for testing"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python promob_parser.py <input_file>")
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        input_text = f.read()

    parser = PromobParser()
    data = parser.parse(input_text)

    # For testing, use default hardware
    output = parser.format_output(
        include_dobradica=['Blum Clip Top Blumotion'],
        include_corredica=['Quadro/Invisível']
    )

    print(output)

    if data.unknown_items:
        print("\n\n--- UNKNOWN ITEMS ---")
        for field, value in data.unknown_items:
            print(f"{field}: {value}")


if __name__ == '__main__':
    main()
