from pyfingerprint.pyfingerprint import PyFingerprint

def cadastrar_crianca():
    try:
        # Conectar ao leitor biométrico
        f = PyFingerprint('/dev/ttyUSB0', 57600)  # Ajuste conforme o seu dispositivo

        # Verificar se o leitor está conectado corretamente
        if ( f.verifyPassword() == False ):
            raise ValueError('Senha do leitor biométrico incorreta!')

        print('Aguarde a impressão digital...')

        # Captura da impressão digital
        while ( f.readImage() == False ):
            pass

        # Converte a imagem em um template de impressão digital
        f.convertImage(0x01)
        result = f.storeTemplate(0x01)

        print(f'Impressão digital registrada com sucesso: {result}')

        # Salvar a impressão digital no banco de dados (armazenar como BLOB)
        # Aqui você precisa salvar no banco o template da impressão digital
        template = f.downloadTemplate(0x01)
        nome = input("Nome da criança: ")

        # Armazenar no banco de dados
        # Aqui você deve usar SQLAlchemy ou outro ORM para inserir os dados no banco
        # Exemplo com SQLAlchemy:
        from models import db, Crianca
        nova_crianca = Crianca(nome=nome, impressao_digital=template)
        db.session.add(nova_crianca)
        db.session.commit()

        print("Cadastro realizado com sucesso!")
    
    except Exception as e:
        print(f'Erro: {e}')
