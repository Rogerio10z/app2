def gerar_relatorio():
    from models import db, Presenca, Crianca
    presencas = db.session.query(Presenca, Crianca).join(Crianca).all()

    for presenca, crianca in presencas:
        print(f'{crianca.nome} - {presenca.data_presenca}')
