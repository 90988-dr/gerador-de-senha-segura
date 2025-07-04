import random
import string
import os # Importa o módulo os para verificar se o arquivo existe

def generate_password(length):
    # Caracteres para a senha: letras (maiúsculas e minúsculas), números e símbolos
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_credentials(username, password, filename="credentials.txt"):
    # Verifica se o arquivo existe e adiciona um cabeçalho se não existir
    file_exists = os.path.exists(filename)
    with open(filename, "a") as f: # "a" para append (adicionar ao final do arquivo)
        if not file_exists or os.path.getsize(filename) == 0: # Adiciona cabeçalho se o arquivo for novo ou vazio
            f.write("Usuário,Senha\n") # Cabeçalho da tabela
        f.write(f"{username},{password}\n") # Escreve o par usuário, senha

if __name__ == "__main__":
    print("--- Gerador de Senhas Seguras ---")
    username = input("Por favor, digite o nome de usuário: ")

    while True:
        try:
            password_length_str = input("Digite o comprimento da senha desejada (número): ")
            password_length = int(password_length_str)
            if password_length <= 0:
                print("O comprimento da senha deve ser um número positivo. Tente novamente.")
            else:
                break # Sai do loop se o comprimento for válido
        except ValueError:
            print("Entrada inválida. Por favor, digite um NÚMERO para o comprimento da senha.")

    secure_password = generate_password(password_length)
    print(f"\nSua senha segura para '{username}' é: {secure_password}")

    save_credentials(username, secure_password)
    print(f"Credenciais (usuário: {username}, senha: {secure_password}) salvas em '{os.path.abspath('credentials.txt')}'")
    print("\n--- Fim do Programa ---")