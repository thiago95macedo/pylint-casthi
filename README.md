# pylint-casthi

Plugin Pylint especializado para análise de código de módulos CasThi.

## Descrição

O `pylint-casthi` é um plugin do Pylint que fornece verificações especializadas para desenvolvimento de módulos CasThi, garantindo qualidade de código, segurança e conformidade com as melhores práticas.

## Instalação

```bash
pip install pylint-casthi
```

## Uso

### Básico
```bash
pylint --load-plugins=pylint_casthi src/
```

### Com arquivo de configuração
```bash
pylint --rcfile=.pylintrc src/
```

### Apenas verificações CasThi
```bash
pylint --load-plugins=pylint_casthi -d all -e casthilint src/
```

## Principais Verificações

### 🔒 Segurança
- **SQL Injection**: Detecta vulnerabilidades de injeção SQL
- **Validação de Inputs**: Verifica validação adequada de dados
- **Controle de Acesso**: Valida permissões e grupos de segurança

### 📋 Manifest e Estrutura
- **Manifest válido**: Verifica estrutura do `__manifest__.py`
- **Versão correta**: Valida formato de versão (16.0.x.y.z)
- **Dependências**: Verifica dependências declaradas
- **Licença**: Valida licença especificada

### 🌐 Traduções
- **Strings traduzíveis**: Detecta textos não traduzidos
- **Métodos de tradução**: Verifica uso correto de `_()` e `_lt()`
- **Formatação**: Valida formatação de strings de tradução

### 🏗️ Arquitetura
- **Imports relativos**: Detecta imports absolutos desnecessários
- **Métodos deprecated**: Identifica uso de métodos obsoletos
- **Herança**: Valida estrutura de herança de modelos
- **Workflows**: Verifica transições de estado

### 📊 Qualidade de Código
- **Nomenclatura**: Valida nomes de variáveis e métodos
- **Complexidade**: Detecta código complexo demais
- **Duplicação**: Identifica código duplicado
- **Documentação**: Verifica docstrings e comentários

## Configuração

### Arquivo `.pylintrc`
```ini
[MASTER]
load-plugins=pylint_casthi

[MESSAGES CONTROL]
disable=all
enable=casthilint,pointless-statement,trailing-newlines

[casthilint]
manifest-required-authors=CasThi
license-allowed=LGPL-3,AGPL-3
```

### Pre-commit Hook
```yaml
repos:
  - repo: https://github.com/thiago95macedo/pylint-casthi
    rev: main
    hooks:
      - id: pylint_casthi
```

## Exemplos de Problemas Detectados

### SQL Injection
```python
# ❌ Problema detectado
query = f"SELECT * FROM res_partner WHERE name = '{name}'"

# ✅ Solução recomendada
query = "SELECT * FROM res_partner WHERE name = %s"
```

### Tradução
```python
# ❌ Problema detectado
message = "User created successfully"

# ✅ Solução recomendada
message = _("User created successfully")
```

### Manifest
```python
# ❌ Problema detectado
{
    'name': 'My Module',
    'version': '1.0.0',  # Formato incorreto
}

# ✅ Solução recomendada
{
    'name': 'My Module',
    'version': '16.0.1.0.0',  # Formato correto
}
```

## Integração com CI/CD

### GitHub Actions
```yaml
name: Lint CasThi Modules
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          pip install pylint-casthi
      - name: Run pylint
        run: |
          pylint --load-plugins=pylint_casthi src/
```

## Desenvolvimento

### Instalação para desenvolvimento
```bash
git clone https://github.com/thiago95macedo/pylint-casthi.git
cd pylint-casthi
pip install -e .
```

### Executar testes
```bash
python -m pytest tests/
```

### Executar linting
```bash
pylint --load-plugins=pylint_casthi src/
```

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença AGPL-3.0 - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Suporte

- **Issues**: [GitHub Issues](https://github.com/thiago95macedo/pylint-casthi/issues)
- **Documentação**: [Wiki do projeto](https://github.com/thiago95macedo/pylint-casthi/wiki)

## CasThi

Este plugin é desenvolvido especificamente para o projeto **CasThi**, uma personalização do Odoo 16 focada no mercado brasileiro.

- **Website**: https://www.casthi.com.br
- **Documentação**: https://docs.casthi.com.br