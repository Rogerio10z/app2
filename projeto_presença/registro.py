def registrar_presenca():
    try:
        # Conectar ao leitor biométrico
        f = PyFingerprint('/dev/ttyUSB0', 57600)

        # Verificar se o leitor está conectado corretamente
        if ( f.verifyPassword() == False ):
            raise ValueError('Senha do leitor biométrico incorreta!')

        # Captura da impressão digital
        print('Aguarde a impressão digital...')
        while ( f.readImage() == False ):
            pass

        # Converte a imagem em um template de impressão digital
        f.convertImage(0x01)

        # Verificar se a impressão digital já está registrada
        result = f.searchTemplate()
        if result >= 0:
            print(f'Impressão digital encontrada: {result}')

            # Registrar presença
            crianca_id = result  # Aqui, é necessário obter o ID da criança
            # Armazenar no banco de dados
            from models import db, Presenca
            nova_presenca = Presenca(crianca_id=crianca_id)
            db.session.add(nova_presenca)
            db.session.commit()

            print("Presença registrada!")
        else:
            print("Impressão digital não reconhecida.")
    
    except Exception as e:
        print(f'Erro: {e}')
