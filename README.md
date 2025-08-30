# 🔐 Simulador de Força Bruta com Proteções de Segurança

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)  
Um simulador educativo de ataques de força bruta que implementa múltiplas camadas de proteção de segurança, incluindo hashing com salt e prevenção contra timing attacks.

---

🛡️ Proteções Implementadas

🔒 Camadas de Segurança
✅ Hashing SHA-256 com Salt - Transforma senhas em valores irreversíveis únicos
✅ Prevenção contra Timing Attacks - Usa hmac.compare_digest() para comparação segura
✅ Contagem de Tentativas - Monitora e limita tentativas de acesso
✅ Não exposição de senhas - Nunca exibe senhas em texto claro

---

🚫 Prevenções Contra Ataques

Rainbow Tables - Salt único torna cada hash diferente
Timing Attacks - Tempo de resposta constante para todas as tentativas
Força Bruta - Controle e monitoramento de tentativas

---

🚀 Como Usar

📥 Clonar o repositório

git clone https://github.com/seu-usuario/password-security-simulator**
cd password-security-simulator

---

2️⃣ Executar o script

Certifique-se de ter o Python 3.x instalado e execute:

python password_simulator.py

---

🛠 Estrutura do Projeto

password-security-simulator/
│── bruteforce_project.py    # Código principal do simulador**
│── README.md                # Documentação do projeto**

---

🎯 Funcionalidades Técnicas

🔄 Processo de Verificação

Geração de salt único com os.urandom(16)
Hash da senha usando SHA-256 com salt
Comparação segura com proteção contra timing attacks
Contagem e limite de tentativas
Retorno seguro sem expor informações sensíveis

---

📊 Lista de Tentativas

O simulador testa contra 15 senhas comuns, incluindo:

Senhas fracas (123456, password)
Senhas médias (Senha123!, Admin2024)
Senha forte (bruteforce31)

---

🗺️ Próximas Melhorias Planejadas

Implementação de PBKDF2 para key stretching
Sistema de rate limiting automático
Interface gráfica web-based
Análise de força de senhas em tempo real
Logs de auditoria e relatórios detalhados

---

📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.
