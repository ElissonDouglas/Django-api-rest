# 🎵 Music Library API

API REST desenvolvida com **Django** e **Django REST Framework** para gerenciamento de uma biblioteca de música. O projeto permite operações completas de CRUD (Create, Read, Update, Delete) para álbuns musicais.

---

## 🚀 Tecnologias Utilizadas

* [Python](https://www.python.org/) (3.10+)
* [Django](https://www.djangoproject.com/) (4.x)
* [Django REST Framework](https://www.django-rest-framework.org/) (DRF)
* [SQLite](https://www.sqlite.org/index.html) (Banco de dados padrão)

---

## ⚙️ Funcionalidades

* **Listagem:** Visualizar todos os álbuns cadastrados.
* **Detalhamento:** Consultar dados de um álbum específico por ID.
* **Cadastro:** Adicionar novos álbuns à biblioteca.
* **Edição:** Atualizar informações de um álbum existente.
* **Remoção:** Excluir álbuns do sistema.

---

## 📦 Instalação e Execução

Siga os passos abaixo para rodar o projeto localmente:

### 1. Clone o repositório
```bash
git clone https://github.com/ElissonDouglas/Django-api-rest.git
cd Django-api-rest
```

### 2. Crie e ative o ambiente virtual
**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute as migrações
```bash
python manage.py migrate
```

### 5. Inicie o servidor
```bash
python manage.py runserver
```

Acesse a API em: `http://127.0.0.1:8000/`

---

## 🔗 Endpoints da API

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/albums/` | Lista todos os álbuns. |
| `POST` | `/api/albums/` | Cria um novo álbum. |
| `GET` | `/api/albums/{id}/` | Detalhes de um álbum específico. |
| `PUT` | `/api/albums/{id}/` | Atualiza um álbum (completo). |
| `DELETE` | `/api/albums/{id}/` | Deleta um álbum. |

---

## 📝 Exemplo de Requisição (JSON)

Exemplo de corpo para criar (`POST`) ou atualizar (`PUT`) um registro:

```json
{
  "title": "Nome do Álbum",
  "artist": "Nome do Artista",
  "year": 2023,
  "genre": "Rock"
}
```

---

## 🤝 Contribuição

1.  Faça um **fork** do projeto.
2.  Crie uma nova branch com as suas alterações: `git checkout -b my-feature`
3.  Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`
4.  Envie as suas alterações: `git push origin my-feature`

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
