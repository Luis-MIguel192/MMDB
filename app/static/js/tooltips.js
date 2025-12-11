// Tooltips para cargos de cinema
document.addEventListener('DOMContentLoaded', function() {
    console.log('Inicializando tooltips para cargos de cinema...');
    
    // Descrições dos cargos no cinema
    const jobDescriptions = {
        'Diretor': 'Responsável pela visão criativa geral do filme, dirigindo atores e coordenando a equipe técnica.',
        'Diretor de Fotografia': 'Responsável pela captura visual do filme, incluindo iluminação, enquadramento e movimento de câmera.',
        'Produtor': 'Gerencia os aspectos financeiros e logísticos da produção, desde o desenvolvimento até a distribuição.',
        'Produtor Executivo': 'Supervisiona múltiplos projetos e fornece financiamento ou recursos para a produção.',
        'Roteirista': 'Escreve o roteiro do filme, criando diálogos, estrutura narrativa e desenvolvimento de personagens.',
        'Editor': 'Monta o filme final, selecionando e organizando as cenas para criar o ritmo e fluxo narrativo.',
        'Compositor': 'Cria a trilha sonora original do filme, compondo músicas que complementam a narrativa.',
        'Designer de Produção': 'Responsável pelo visual geral do filme, incluindo cenários, figurinos e paleta de cores.',
        'Diretor de Arte': 'Supervisiona a criação dos elementos visuais, trabalhando com cenógrafos e decoradores.',
        'Figurinista': 'Desenha e coordena os figurinos dos personagens, contribuindo para a caracterização.',
        'Maquiador': 'Responsável pela maquiagem dos atores, incluindo efeitos especiais e caracterização.',
        'Supervisor de Efeitos Visuais': 'Coordena a criação de efeitos digitais e visuais especiais do filme.',
        'Mixador de Som': 'Responsável pela mixagem final do áudio, balanceando diálogos, música e efeitos sonoros.',
        'Ator': 'Interpreta um personagem no filme, trazendo vida às palavras do roteiro através da performance.',
        'Atriz': 'Interpreta um personagem no filme, trazendo vida às palavras do roteiro através da performance.',
        'Diretor Assistente': 'Auxilia o diretor na coordenação do set e no cumprimento do cronograma de filmagem.',
        'Operador de Câmera': 'Opera as câmeras durante as filmagens, seguindo as direções do diretor de fotografia.',
        'Gaffer': 'Chefe da equipe de iluminação, responsável por implementar o plano de iluminação do filme.',
        'Continuísta': 'Garante a continuidade visual entre as cenas, anotando detalhes de figurino, maquiagem e cenário.',
        'Casting Director': 'Responsável pela seleção e contratação dos atores para os diversos papéis do filme.'
    };

    // Função para inicializar tooltips
    function initializeTooltips() {
        // Buscar todos os elementos que podem ter tooltips
        const jobElements = document.querySelectorAll('.job-role, strong:contains("Diretor"), strong:contains("Ator"), strong:contains("Atriz"), strong:contains("Produtor")');
        
        jobElements.forEach(function(element) {
            const cargo = element.getAttribute('data-cargo') || element.textContent.trim();
            const description = jobDescriptions[cargo];
            
            if (description) {
                // Adicionar atributos necessários
                element.classList.add('job-role');
                element.setAttribute('data-bs-toggle', 'tooltip');
                element.setAttribute('data-bs-placement', 'top');
                element.setAttribute('data-cargo', cargo);
                element.setAttribute('title', description);
                
                // Inicializar tooltip do Bootstrap
                if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
                    new bootstrap.Tooltip(element, {
                        placement: 'top',
                        trigger: 'hover focus'
                    });
                }
                
                console.log('Tooltip inicializado para:', cargo);
            }
        });
    }

    // Inicializar tooltips
    initializeTooltips();
    
    // Reinicializar tooltips quando o conteúdo mudar (para SPAs)
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length > 0) {
                initializeTooltips();
            }
        });
    });
    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
    
    console.log('Sistema de tooltips inicializado!');
});