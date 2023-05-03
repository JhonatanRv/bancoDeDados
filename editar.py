from conexao import conectar


conn = conectar()

cursor = conn.cursor()

busca = input("Digite o nome do estado que deseja editar: ")


sql = "SELECT * FROM estado WHERE nome like %s"

val = ("%"+ busca + "%",)

cursor.execute(sql, val)

result = cursor.fetchone()


if result:
    codigo = result[0]
    nome_antigo = result[1]
    print(f"O nome atual do estado é '{nome_antigo}'.")
    novo_nome = input("Digite o novo nome do estado: ")
    
    
    while not novo_nome:
        novo_nome = input("Digite o novo nome do estado: ")
        
    confimacao = input(f"Tem certeza que deseja alterar o nome '{nome_antigo}' para '{novo_nome}'? (s/n) ")

    if confimacao.lower() == "s":
        sql = "UPDATE estado SET nome = %s WHERE codigo = %s"
        val = (novo_nome, codigo)
        cursor.execute(sql, val)
        conn.commit()
        print(f"O nome do estado '{nome_antigo}' foi atualizado para '{novo_nome}' com sucesso")
        
    else:
        print("Operação cancela pelo usuário.")
        
        
else:
    print("Não foi encontrado nenhum estado com o nome informado.")
    
    
conn.close()