"""Blueprint para rotas relacionadas a filmes."""

from flask import Blueprint, render_template
from app.models.filmes import Filme, Pessoa, Elenco

filmes_bp = Blueprint('filmes',
                     __name__,
                     url_prefix='/filmes',
                     template_folder='templates')


@filmes_bp.route("/")
def listar_filmes():
    """Lista todos os filmes."""
    filmes = Filme.query.all()
    return render_template("filmes/listar.jinja2",
                          title="Filmes",
                          filmes=filmes)


@filmes_bp.route("/<uuid:filme_id>")
def detalhes_filme(filme_id):
    """Mostra detalhes de um filme específico."""
    filme = Filme.get_by_id(filme_id, raise_if_not_found=True)
    
    # Buscar elenco do filme
    elenco = Elenco.query.filter_by(filme_id=filme_id).order_by(Elenco.ordem).all()
    
    return render_template("filmes/detalhes.jinja2",
                          title=filme.titulo,
                          filme=filme,
                          elenco=elenco)


@filmes_bp.route("/pessoas")
def listar_pessoas():
    """Lista todas as pessoas."""
    pessoas = Pessoa.query.all()
    return render_template("filmes/pessoas.jinja2",
                          title="Pessoas",
                          pessoas=pessoas)


@filmes_bp.route("/pessoas/<uuid:pessoa_id>")
def detalhes_pessoa(pessoa_id):
    """Mostra detalhes de uma pessoa específica."""
    pessoa = Pessoa.get_by_id(pessoa_id, raise_if_not_found=True)
    
    # Buscar participações da pessoa
    participacoes = Elenco.query.filter_by(pessoa_id=pessoa_id).order_by(Elenco.ordem).all()
    
    return render_template("filmes/pessoa_detalhes.jinja2",
                          title=pessoa.nome,
                          pessoa=pessoa,
                          participacoes=participacoes)


@filmes_bp.route("/populares")
def filmes_populares():
    """Lista filmes populares (ordenados por ano de lançamento decrescente)."""
    filmes = Filme.query.order_by(Filme.ano_lancamento.desc()).all()
    return render_template("filmes/listar.jinja2",
                          title="Filmes Populares",
                          filmes=filmes)


@filmes_bp.route("/em-cartaz")
def filmes_em_cartaz():
    """Lista filmes em cartaz (filmes mais recentes)."""
    from datetime import datetime
    ano_atual = datetime.now().year
    filmes = Filme.query.filter(Filme.ano_lancamento >= ano_atual - 2).order_by(Filme.ano_lancamento.desc()).all()
    return render_template("filmes/listar.jinja2",
                          title="Filmes em Cartaz",
                          filmes=filmes)


@filmes_bp.route("/pessoas/atores")
def listar_atores():
    """Lista apenas atores."""
    atores_ids = Elenco.query.filter(Elenco.cargo.in_(['Ator', 'Atriz'])).with_entities(Elenco.pessoa_id).distinct()
    pessoas = Pessoa.query.filter(Pessoa.id.in_(atores_ids)).all()
    return render_template("filmes/pessoas.jinja2",
                          title="Atores",
                          pessoas=pessoas)


@filmes_bp.route("/pessoas/equipe-tecnica")
def listar_equipe_tecnica():
    """Lista equipe técnica (diretores, produtores, etc.)."""
    equipe_ids = Elenco.query.filter(~Elenco.cargo.in_(['Ator', 'Atriz'])).with_entities(Elenco.pessoa_id).distinct()
    pessoas = Pessoa.query.filter(Pessoa.id.in_(equipe_ids)).all()
    return render_template("filmes/pessoas.jinja2",
                          title="Equipe Técnica",
                          pessoas=pessoas)


@filmes_bp.route("/genero/<genero>")
def filmes_por_genero(genero):
    """Lista filmes por gênero específico."""
    # Decodificar o gênero da URL
    genero_decoded = genero.replace('-', ' ').title()
    
    # Buscar filmes que contenham o gênero
    filmes = Filme.query.filter(Filme.genero.contains(genero_decoded)).all()
    
    return render_template("filmes/listar.jinja2",
                          title=f"Filmes de {genero_decoded}",
                          filmes=filmes)


@filmes_bp.route("/pessoas/cargo/<cargo>")
def pessoas_por_cargo(cargo):
    """Lista pessoas por cargo específico."""
    # Decodificar o cargo da URL
    cargo_decoded = cargo.replace('-', ' ').title()
    
    # Buscar pessoas com esse cargo
    pessoas_ids = Elenco.query.filter(Elenco.cargo.ilike(f'%{cargo_decoded}%')).with_entities(Elenco.pessoa_id).distinct()
    pessoas = Pessoa.query.filter(Pessoa.id.in_(pessoas_ids)).all()
    
    return render_template("filmes/pessoas.jinja2",
                          title=f"{cargo_decoded}s",
                          pessoas=pessoas)


@filmes_bp.route("/generos")
def listar_generos():
    """Lista todos os gêneros disponíveis."""
    from sqlalchemy import func
    
    # Buscar todos os gêneros únicos
    generos_raw = Filme.query.with_entities(Filme.genero).filter(Filme.genero.isnot(None)).distinct().all()
    
    # Processar gêneros (alguns filmes têm múltiplos gêneros separados por vírgula)
    generos_set = set()
    for genero_tuple in generos_raw:
        genero = genero_tuple[0]
        if genero:
            # Dividir por vírgula e limpar espaços
            for g in genero.split(','):
                generos_set.add(g.strip())
    
    generos = sorted(list(generos_set))
    
    return render_template("filmes/generos.jinja2",
                          title="Gêneros",
                          generos=generos)


@filmes_bp.route("/cargos")
def listar_cargos():
    """Lista todos os cargos disponíveis."""
    from sqlalchemy import func
    
    # Buscar todos os cargos únicos
    cargos = Elenco.query.with_entities(Elenco.cargo).distinct().order_by(Elenco.cargo).all()
    cargos_list = [cargo[0] for cargo in cargos if cargo[0]]
    
    return render_template("filmes/cargos.jinja2",
                          title="Cargos",
                          cargos=cargos_list)


@filmes_bp.route("/buscar")
def buscar():
    """Busca filmes e pessoas."""
    from flask import request, flash
    query = request.args.get('q', '').strip()
    
    # Teste de mensagem flash para verificar visibilidade
    if request.args.get('test_msg'):
        flash('Esta é uma mensagem de teste para verificar a visibilidade!', 'success')
        flash('Mensagem de informação para teste', 'info')
        flash('Mensagem de aviso para teste', 'warning')
    
    if not query:
        return render_template("filmes/buscar.jinja2",
                              title="Buscar",
                              query="",
                              filmes=[],
                              pessoas=[])
    
    # Buscar filmes
    filmes = Filme.query.filter(
        (Filme.titulo.contains(query)) | 
        (Filme.titulo_original.contains(query)) |
        (Filme.sinopse.contains(query))
    ).all()
    
    # Buscar pessoas
    pessoas = Pessoa.query.filter(
        (Pessoa.nome.contains(query)) |
        (Pessoa.nome_completo.contains(query)) |
        (Pessoa.biografia.contains(query))
    ).all()
    
    return render_template("filmes/buscar.jinja2",
                          title=f"Buscar: {query}",
                          query=query,
                          filmes=filmes,
                          pessoas=pessoas)