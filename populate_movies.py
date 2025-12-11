#!/usr/bin/env python3
"""Script para popular o banco de dados com filmes, pessoas e elenco de exemplo."""

from datetime import date
from app import create_app
from app.infra.modulos import db
from app.models.filmes import Filme, Pessoa, Elenco

def populate_database():
    """Popula o banco com dados de exemplo."""
    
    # Criar pessoas (atores, diretores)
    pessoas = [
        # Matrix
        Pessoa(
            nome="Keanu Reeves",
            nome_completo="Keanu Charles Reeves",
            data_nascimento=date(1964, 9, 2),
            nacionalidade="Canadense",
            biografia="Ator canadense conhecido por seus papéis em Matrix, John Wick e Speed.",
            foto_url="https://image.tmdb.org/t/p/w500/4D0PpNI0kmP58hgrwGC3wCjxhnm.jpg"
        ),
        Pessoa(
            nome="Laurence Fishburne",
            nome_completo="Laurence John Fishburne III",
            data_nascimento=date(1961, 7, 30),
            nacionalidade="Americano",
            biografia="Ator americano conhecido por Morpheus em Matrix e outros papéis icônicos.",
            foto_url="https://image.tmdb.org/t/p/w500/8suOhUmPbfKqDQ17jQ1Gy0mI3P4.jpg"
        ),
        Pessoa(
            nome="Carrie-Anne Moss",
            nome_completo="Carrie-Anne Moss",
            data_nascimento=date(1967, 8, 21),
            nacionalidade="Canadense",
            biografia="Atriz canadense famosa por interpretar Trinity na trilogia Matrix.",
            foto_url="https://image.tmdb.org/t/p/w500/xD4jTA3KmVp5Rq3aHcymL9DUGjD.jpg"
        ),
        Pessoa(
            nome="Lana Wachowski",
            nome_completo="Lana Wachowski",
            data_nascimento=date(1965, 6, 21),
            nacionalidade="Americana",
            biografia="Diretora americana, co-criadora da trilogia Matrix.",
            foto_url=None
        ),
        Pessoa(
            nome="Lilly Wachowski",
            nome_completo="Lilly Wachowski",
            data_nascimento=date(1967, 12, 29),
            nacionalidade="Americana",
            biografia="Diretora americana, co-criadora da trilogia Matrix.",
            foto_url=None
        ),
        
        # Inception
        Pessoa(
            nome="Leonardo DiCaprio",
            nome_completo="Leonardo Wilhelm DiCaprio",
            data_nascimento=date(1974, 11, 11),
            nacionalidade="Americano",
            biografia="Ator americano vencedor do Oscar, conhecido por Titanic, Inception e The Revenant.",
            foto_url="https://image.tmdb.org/t/p/w500/wo2hJpn04vbtmh0B9utCFdsQhxM.jpg"
        ),
        Pessoa(
            nome="Marion Cotillard",
            nome_completo="Marion Cotillard",
            data_nascimento=date(1975, 9, 30),
            nacionalidade="Francesa",
            biografia="Atriz francesa vencedora do Oscar por La Vie en Rose.",
            foto_url=None
        ),
        Pessoa(
            nome="Tom Hardy",
            nome_completo="Edward Thomas Hardy",
            data_nascimento=date(1977, 9, 15),
            nacionalidade="Britânico",
            biografia="Ator britânico conhecido por Inception, Mad Max e Venom.",
            foto_url="https://image.tmdb.org/t/p/w500/d81K0RH8UX7tZj49tZaQhZ9ewH.jpg"
        ),
        Pessoa(
            nome="Christopher Nolan",
            nome_completo="Christopher Edward Nolan",
            data_nascimento=date(1970, 7, 30),
            nacionalidade="Britânico",
            biografia="Diretor britânico conhecido por filmes complexos como Inception, Interstellar e The Dark Knight.",
            foto_url="https://image.tmdb.org/t/p/w500/xuAIuYSmsUzKlUMBFGVZaWsY3DZ.jpg"
        ),
        
        # Pulp Fiction
        Pessoa(
            nome="John Travolta",
            nome_completo="John Joseph Travolta",
            data_nascimento=date(1954, 2, 18),
            nacionalidade="Americano",
            biografia="Ator americano conhecido por Grease, Saturday Night Fever e Pulp Fiction.",
            foto_url="https://image.tmdb.org/t/p/w500/9GVufE87MMIrSn0CbJFLudkALdL.jpg"
        ),
        Pessoa(
            nome="Samuel L. Jackson",
            nome_completo="Samuel Leroy Jackson",
            data_nascimento=date(1948, 12, 21),
            nacionalidade="Americano",
            biografia="Ator americano prolífico, conhecido por Pulp Fiction, Snakes on a Plane e filmes da Marvel.",
            foto_url="https://image.tmdb.org/t/p/w500/AiAYAqwpM5xmiFrAIeQvUXDCVvo.jpg"
        ),
        Pessoa(
            nome="Uma Thurman",
            nome_completo="Uma Karuna Thurman",
            data_nascimento=date(1970, 4, 29),
            nacionalidade="Americana",
            biografia="Atriz americana conhecida por Pulp Fiction e Kill Bill.",
            foto_url="https://image.tmdb.org/t/p/w500/xuxgPXyv6KjUHIM8cZaxx4ry25L.jpg"
        ),
        Pessoa(
            nome="Quentin Tarantino",
            nome_completo="Quentin Jerome Tarantino",
            data_nascimento=date(1963, 3, 27),
            nacionalidade="Americano",
            biografia="Diretor americano conhecido por seu estilo único em filmes como Pulp Fiction, Kill Bill e Django Unchained.",
            foto_url="https://image.tmdb.org/t/p/w500/1gjcpAa99FAOWGnrUvHEXXsRs7o.jpg"
        )
    ]
    
    # Adicionar pessoas ao banco
    for pessoa in pessoas:
        db.session.add(pessoa)
    
    db.session.flush()  # Para obter os IDs
    
    # Criar filmes
    filmes = [
        Filme(
            titulo="Matrix",
            titulo_original="The Matrix",
            sinopse="Um hacker descobre que a realidade como ele a conhece é na verdade uma simulação controlada por máquinas.",
            ano_lancamento=1999,
            data_lancamento=date(1999, 3, 31),
            duracao_minutos=136,
            genero="Ficção Científica, Ação",
            classificacao="R",
            poster_url="https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"
        ),
        Filme(
            titulo="A Origem",
            titulo_original="Inception",
            sinopse="Um ladrão que invade sonhos recebe a tarefa impossível de plantar uma ideia na mente de alguém.",
            ano_lancamento=2010,
            data_lancamento=date(2010, 7, 16),
            duracao_minutos=148,
            genero="Ficção Científica, Thriller",
            classificacao="PG-13",
            poster_url="https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg"
        ),
        Filme(
            titulo="Pulp Fiction: Tempo de Violência",
            titulo_original="Pulp Fiction",
            sinopse="Histórias interconectadas de criminosos, boxeadores e gangsters em Los Angeles.",
            ano_lancamento=1994,
            data_lancamento=date(1994, 10, 14),
            duracao_minutos=154,
            genero="Crime, Drama",
            classificacao="R",
            poster_url="https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg"
        )
    ]
    
    # Adicionar filmes ao banco
    for filme in filmes:
        db.session.add(filme)
    
    db.session.flush()  # Para obter os IDs
    
    # Criar elenco
    elencos = [
        # Matrix
        Elenco(filme=filmes[0], pessoa=pessoas[0], cargo="Ator", personagem="Neo", ordem=1),
        Elenco(filme=filmes[0], pessoa=pessoas[1], cargo="Ator", personagem="Morpheus", ordem=2),
        Elenco(filme=filmes[0], pessoa=pessoas[2], cargo="Atriz", personagem="Trinity", ordem=3),
        Elenco(filme=filmes[0], pessoa=pessoas[3], cargo="Diretor", ordem=1),
        Elenco(filme=filmes[0], pessoa=pessoas[4], cargo="Diretor", ordem=2),
        
        # Inception
        Elenco(filme=filmes[1], pessoa=pessoas[5], cargo="Ator", personagem="Dom Cobb", ordem=1),
        Elenco(filme=filmes[1], pessoa=pessoas[6], cargo="Atriz", personagem="Mal", ordem=2),
        Elenco(filme=filmes[1], pessoa=pessoas[7], cargo="Ator", personagem="Eames", ordem=3),
        Elenco(filme=filmes[1], pessoa=pessoas[8], cargo="Diretor", ordem=1),
        
        # Pulp Fiction
        Elenco(filme=filmes[2], pessoa=pessoas[9], cargo="Ator", personagem="Vincent Vega", ordem=1),
        Elenco(filme=filmes[2], pessoa=pessoas[10], cargo="Ator", personagem="Jules Winnfield", ordem=2),
        Elenco(filme=filmes[2], pessoa=pessoas[11], cargo="Atriz", personagem="Mia Wallace", ordem=3),
        Elenco(filme=filmes[2], pessoa=pessoas[12], cargo="Diretor", ordem=1),
    ]
    
    # Adicionar elenco ao banco
    for elenco in elencos:
        db.session.add(elenco)
    
    # Commit de tudo
    db.session.commit()
    
    print("✅ Banco de dados populado com sucesso!")
    print(f"📽️ {len(filmes)} filmes adicionados")
    print(f"👥 {len(pessoas)} pessoas adicionadas")
    print(f"🎭 {len(elencos)} registros de elenco adicionados")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        populate_database()