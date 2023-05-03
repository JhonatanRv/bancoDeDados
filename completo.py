from conexao import conectar


def listar(conn, cursor):
    
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM estado")
    
    resultados = cursor.fetchall()
    
    for resultado in resultados:
        print(resultado)
        
    cursor.close()
    conn.close()
    
    
def inserir(codigo, nome):
    
    conn = conectar()
    cursor = conn.cursor()
    
    sql = "INSERT INTO estado (codigo, nome) VALUES (%s, %s)"
    val = (codigo, nome)
    cursor.execute(sql, val)
    
    conn.commit()
    
    print("Registro inserido com sucesso.")
    
    cursor.close()
    conn.close()
    
    
    
def atualizar(codigo, novo_nome):
    
    conn = conectar()
    cursor = conn.cursor()
    
    sql = "UPDATE estado SET nome = %s WHERE codigo = %s"
    val = (novo_nome, codigo)
    cursor.execute(sql, val)
    
    conn.commit()
    
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado")
    else:
        print("Atualizado com sucesso")
        
        
    cursor.close()
    conn.close()
    
    
    
    
def deletar(codigo):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para deletar o registro
    sql = "DELETE FROM estado WHERE codigo = %s"
    val = (codigo,)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi deletado
    if cursor.rowcount == 0:
        print("Nenhum registro deletado.")
    else:
        print("Registro deletado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()
    
    
    

conn = conectar()

cursor = conn.cursor()
while True:
    print("O que deseja fazer?")
    print("1 - Listar estados")
    print("2 - Inserir estados")
    print("3 - Atualizar estados")
    print("4 - Deletar estados")
    print("0 - Sair")
    
    op = int(input("Digite o número da opção desejada: "))
    
    
    if op == 1:
        listar(conn, cursor)
        
    
    elif op == 2:  
        codigo = int(input("Digite o código do novo estado: "))
        nome = input("Digite o nome do novo estado: ")
        inserir(codigo, nome)
        
    elif op == 3:  
        codigo = int(input("Digite o código do novo estado: "))
        nome = input("Digite o novo nome do estado: ")
        atualizar(codigo, nome)
        
        
    elif op == 4:  
        codigo = int(input("Digite o código do estado que deseja deletar: "))
        deletar(codigo)
        
    elif op == 0:
        print("Você escolheu sair")
        break
    
    else: 
        print("Escolha uma opção válida")
        
        
        
    conn.close
    
    
    
    
    
    