# **Vesper:** Robô Bartender

Trabalho de Interação Humano-Robô (IHR) apresentado ao Centro Universitário [FEI](https://portal.fei.edu.br/), como parte dos requisitos necessários para aprovação na disciplina de Interação Humano-Robô (IHR) (CCR230) do curso de Engenharia de Robôs, orientado pelo Prof. Dr. [Fagner de Assis Moura Pimentel](https://github.com/fagnerpimentel).

### Componentes do Grupo

- João Victor de Assis Segantin RA:11.120.378-2

### Resumo

O robô Vesper é um bartender automatizado desenvolvido para operar em restaurantes de padrão médio-alto com perfil tecnológico. Ele é responsável pela preparação e distribuição de bebidas diretamente no balcão do bar, onde os próprios clientes se dirigem para realizar seus pedidos. O Vesper atua de forma fixa, com braços robóticos responsáveis pela manipulação precisa dos insumos e preparo das bebidas. Sua aplicação visa otimizar o tempo de atendimento, reduzir a carga de trabalho dos garçons e garantir padronização e agilidade na entrega dos pedidos. Além disso, o robô conta com interação verbal por meio de alto-falantes e elementos de interação não verbal e espacial, promovendo uma experiência moderna e envolvente para os clientes.

### Introdução

A automação tem se consolidado como uma das principais tendências para enfrentar os desafios operacionais em diversos setores da economia, especialmente naqueles em que a agilidade e a eficiência no atendimento são fatores críticos para a satisfação do cliente. No setor gastronômico, restaurantes de médio a alto padrão têm buscado formas de incorporar tecnologias que agreguem valor à experiência dos frequentadores sem comprometer a qualidade do serviço humano. Um dos principais gargalos identificados nesse contexto é o atendimento em bares, onde a preparação e a entrega de bebidas durante horários de pico podem gerar filas, atrasos e sobrecarga dos garçons.

A proposta de robôs bartenders emerge como uma solução estratégica e inovadora diante dessa realidade. Além de aliviar a carga de trabalho da equipe humana, esses sistemas automatizados contribuem para a padronização das bebidas, reduzem falhas humanas e proporcionam uma experiência diferenciada ao cliente, alinhada às expectativas de um público cada vez mais conectado com soluções tecnológicas.

Neste cenário, foi desenvolvido o Vesper, um robô bartender fixo, projetado para operar em um bar dentro de um restaurante tecnologicamente sofisticado. O Vesper é responsável por receber os pedidos de bebidas diretamente dos clientes, preparar e entregá-las de maneira precisa e eficiente. Equipado com braços robóticos, sensores, saídas de áudio para interação verbal e cortinas de segurança para proteção dos usuários, ele representa uma fusão entre funcionalidade e design. Apesar de ser uma estação fixa, sua interação é pensada para transmitir simpatia e modernidade, sem causar estranhamento ao público.

### Publico Alvo

O robô bartender Vesper foi desenvolvido para atender um público que frequenta restaurantes de padrão médio-alto, em ambientes onde a tecnologia e a sofisticação fazem parte da proposta de valor do estabelecimento. Esse público busca agilidade no atendimento, praticidade no processo de pedidos e, ao mesmo tempo, experiências diferenciadas e inovadoras. Além disso, o Vesper também interage com os colaboradores do restaurante, principalmente os garçons responsáveis pelo suporte logístico da operação.

### Personas
Persona Primária – Rafael, 28 anos, publicitário
Contexto social e econômico: Profissional de classe média-alta, conectado às tendências de inovação. Frequenta bares, eventos sociais e ambientes modernos. Valoriza experiências tecnológicas, práticas e diferenciadas.
Cultura e comportamento: É ativo em redes sociais, gosta de registrar experiências marcantes e compartilhar com amigos. Demonstra interesse por inovações, automação e ambientes interativos. Prefere atendimento rápido e organizado, e tem baixa tolerância a atrasos ou confusão.

O que o robô precisa saber antes de iniciar a tarefa:
O tipo de bebida desejada (menu acessível e objetivo)
Se o cliente é maior de idade (confirmação obrigatória para bebidas alcoólicas)
Se há restrições alimentares ou preferências (ex: sem álcool, sem gelo, etc.)

Persona Secundária – João, 40 anos, garçom
Contexto social e econômico: Profissional com ampla experiência em restaurantes de médio a alto padrão. Atua em um ambiente onde a eficiência operacional é crucial. Tem domínio de tarefas logísticas e conhecimento básico em sistemas automatizados.
Cultura e comportamento: Organizado, prático e colaborativo. Está acostumado com novas tecnologias e valoriza instruções claras. Preza pela segurança no ambiente de trabalho e pelo bom funcionamento dos equipamentos sob sua supervisão.

O que o robô precisa saber antes de iniciar a tarefa:
Se há itens em falta no estoque interno (detectado por sensores do próprio robô)
Quais insumos devem ser reabastecidos (ex: gelo, bebidas, copos)
Onde ficam os insumos, facilitando a reposição
Que alertas visuais ou sonoros devem ser ativados para sinalizar falhas ou baixo nível de estoque

# Outras Personas
Gestores do restaurante: Avaliam o impacto do Vesper na operação, a satisfação dos clientes e a viabilidade econômica do investimento em automação.
Técnicos de manutenção: Responsáveis por atualizações de software, calibração dos braços, sensores e integridade da cortina de segurança.

# Personas que não devem interagir com o robô
Crianças e adolescentes (menores de 18 anos):
O Vesper foi projetado para atender exclusivamente adultos. A interação com menores de idade é proibida por razões legais (venda de bebidas alcoólicas) e de segurança física. Como o robô possui partes móveis e elementos automatizados, existe risco de acidente caso crianças se aproximem indevidamente. Para isso, o projeto prevê a implementação de barreiras físicas como cortina de segurança, delimitação de área e, futuramente, sistemas de verificação de idade.
### Mapa de empatia

![Mapa Empatia](empatia_Rafael.png)

### Persona Primária: Rafael, 28 anos, publicitário
O que ele PENSA E SENTE?
Rafael se sente empolgado com a experiência de um robô no ambiente de lazer. Quer diversão com eficiência e um toque de inovação. Sente-se seguro e curioso com o robô entregando bebidas. Espera uma interação amigável e tranquila.

O que ele ESCUTA?
Conversas animadas entre amigos sobre o robô. Sons ambientes do bar, música moderna. Influenciadores nas redes comentando sobre “o bar do robô”.

O que ele VÊ?
Ambiente iluminado, moderno, com pessoas socializando, luzes e o Vesper se movimentando com suavidade. Observa outros interagindo com o robô de forma positiva.

O que ele FALA E FAZ?
Comenta com amigos sobre a inovação. Tira fotos e vídeos do robô. Pode acenar ou se aproximar, mantendo uma distância confortável e respeitosa. Ri ou faz comentários sobre “estar no futuro”.

DOR:
Esperar muito tempo pelo atendimento. Sentir que o robô é brusco ou ameaçador. Não entender como funciona a interação.

GANHOS:
Atendimento divertido, automatizado, rápido e seguro. Experiência diferenciada e memorável. Praticidade no recebimento da bebida.

![Mapa Empatia](empatia_Joao.png)

### Persona Secundária: João, 40 anos, garçom
O que ele PENSA E SENTE?
João vê o robô como uma ferramenta de apoio. Sente-se mais eficiente com o uso do Vesper, mas também carrega a responsabilidade de manter o robô abastecido e funcionando. Quer evitar erros ou falhas operacionais.

O que ele ESCUTA?
Instruções da equipe técnica ou do supervisor. Feedback dos colegas sobre o funcionamento do robô. Clientes comentando sobre a experiência com curiosidade e entusiasmo.

O que ele VÊ?
A base operacional do robô, com reservatórios e compartimentos de bebida. O fluxo de pessoas no salão e as rotas do robô em operação. Painéis de status ou sinais visuais no Vesper indicando necessidades.

O que ele FALA E FAZ?
Reabastece compartimentos, faz verificações rápidas, limpa sensores ou superfície quando necessário. Comenta entre colegas sobre a praticidade ou os desafios. Relata qualquer problema ao suporte técnico.

DOR:
Atrasos no reabastecimento, mau funcionamento ou dúvidas técnicas. Dificuldade de acesso ao compartimento do robô. Falta de treinamento adequado.

GANHOS:
Redução de esforço físico, agilidade no atendimento. Mais tempo para focar em outras demandas. Reconhecimento por trabalhar em um ambiente moderno.

### Contexto de uso
Ambiente de interação:
O Vesper opera em ambientes sociais fechados como bares temáticos, lounges modernos, feiras tecnológicas, eventos corporativos ou ambientes universitários voltados à inovação. O espaço possui fluxo moderado de pessoas, iluminação controlada. Há uma área reservada para reabastecimento supervisionada por funcionários.

Contexto social, econômico e cultural:
O ambiente é composto majoritariamente por adultos e jovens adultos além de profissionais de classe média urbana, com interesse por tecnologia, inovação e experiências diferenciadas. Culturalmente, trata-se de um público habituado a novidades digitais. O uso do robô agrega um diferencial futurista ao local e reforça o posicionamento da marca como inovadora.

# Informações que o robô deve saber antes de iniciar a tarefa:
Mapeamento do ambiente: 
Como o Vesper é um robô fixo, o mapeamento do ambiente não envolve rotas de locomoção ou áreas de circulação. Sua interação com o espaço físico é extremamente limitada, sendo necessária apenas uma zona frontal acessível e segura para que o usuário retire a bebida com conforto.

Controle de volume:
Adequação do nível dos speakers ao ambiente (evitando sons altos em locais mais silenciosos ou ao se aproximar dos clientes).

Presença de obstáculos: 
Como o Vesper não possui mobilidade e está fixo em sua base, ele não precisa monitorar rotas ou obstáculos em caminhos de deslocamento. No entanto, para garantir a operação segura e fluida, é importante que a área imediatamente em frente ao robô esteja sempre desobstruída.

Nível de bebida no compartimento:
Evitar iniciar entregas com estoque insuficiente.

Estado do ambiente: 
Nível de iluminação, se há som ambiente alto, clima (para adaptar eventuais mensagens ou tom de voz).

## Jornada do usuário

Narrativa:
No ambiente de um bar tecnológico, o cliente se dirige até o balcão, onde encontra o robô Vesper posicionado de forma fixa. O robô está protegido por uma cortina de segurança transparente que delimita claramente seu espaço de atuação, impedindo contato direto entre os usuários e suas partes móveis enquanto estiver em operação. A ativação acontece exclusivamente por meio do toque no tablet localizado na frente da base do robô, fora da zona de segurança.

Jornada passo a passo:

Início da interação (verbal):
O cliente toca na tela do tablet para iniciar o pedido. Isso desperta o sistema do Vesper, que responde de forma simpática por meio dos alto-falantes:
“Sejam bem-vindos!!”

Escolha da bebida (verbal):
A tela exibe o menu de bebidas. Enquanto o cliente navega, o robô continua guiando a interação verbalmente:
“Por favor, selecione no tablet abaixo a sua bebida! Basta selecionar a bebida e concluir o pedido. Depois só esperar que vou começar o preparo!”

Preparo da bebida (não-verbal):
O Vesper inicia o processo de preparo automatizado dentro da zona protegida por cortina. Seus braços se movem de forma suave e controlada. LEDs indicam o status da operação.

Entrega (verbal e não-verbal):
Com a bebida pronta, o braço do robô estende cuidadosamente o copo até a borda da área segura, posicionando-o na altura de retirada. Nesse momento, o robô anuncia:
“Bebida pronta! Pegue com cuidado dos meus dedos, pode escorregar!”

O cliente apenas estende o braço até a área permitida e retira o copo.

Encerramento (verbal):
Após a retirada do copo, o robô volta para sua posição inicial e agradece:
“Espero que tenha gostado! Obrigado e volte sempre!”

Ambiente durante a interação:

O bar permanece funcional, com música ambiente e movimento moderado.

A cortina de segurança delimita claramente o espaço do robô, reforçando a segurança da interação.

Não há movimentação do robô no espaço físico

A única interface física acessível ao cliente é o tablet, que fica fora da zona de segurança.

Resumo das interações:

Interações verbais:

“Sejam bem-vindos!!”

“Por favor selecione no tablet abaixo a sua bebida!”

“Basta selecionar a bebida e concluir pedido.”

“Depois só esperar que vou começar o preparo!”

“Bebida pronta!”

“Pegue com cuidado dos meus dedos, pode escorregar!”

“Espero que tenha gostado!”

“Obrigado e volte sempre!”

Interações não-verbais:

Luzes LED indicam status do preparo

Braço do robô entrega o copo até a borda da área segura

Interações espaciais:

Extremamente limitadas e restritas à zona frontal do robô

Usuário apenas estende a mão para pegar a bebida em ponto seguro

A cortina de segurança impede qualquer outro tipo de aproximação

## Análise de concorrência

Para o desenvolvimento do robô bartender Vesper, foram estudadas três plataformas já existentes que exercem funções semelhantes no mercado de automação de serviços de bebidas. A seguir, apresentamos uma análise comparativa entre elas e o Vesper:

Concorrentes diretos:

a) Makr Shakr
Descrição: Robô bartender com braços industriais (tipo KUKA) que preparam drinks em bares automatizados. Utilizado em cruzeiros, eventos e estabelecimentos premium.

Pontos positivos:

Alto grau de automação

Capacidade de preparo personalizado de coquetéis

Design chamativo que atrai o público

Pontos negativos:

Alto custo de implementação e manutenção

Estrutura complexa e de grandes dimensões

Pouca interação social real (é mais espetáculo do que serviço cotidiano)

b) BierPaulii Robot
Descrição: Robô fixo alemão voltado para o serviço de cervejas. Ele abre garrafas e serve canecas automaticamente.

Pontos positivos:

Simples, direto e funcional

Excelente para ambientes de alto volume (festas, festivais, etc.)

Interação rápida e divertida

Pontos negativos:

Limitado a bebidas específicas (cervejas)

Pouca personalização de atendimento

Aparência rústica e industrial

c) Schank-Robot
Descrição: Sistema de autosserviço de bebidas que integra robótica e esteiras automatizadas. Voltado para grandes eventos e feiras.

Pontos positivos:

Alta produtividade em grande escala

Ideal para ambientes com alto fluxo e pouca personalização

Baixo tempo de espera

Pontos negativos:

Interação limitada ao digital

Não proporciona experiência personalizada ou estética

Pouco atrativo em ambientes sofisticados

Plataforma similar ao Vesper (mesmo público e funcionalidades):
O Makr Shakr é a plataforma mais próxima do Vesper em termos de mercado-alvo e funcionalidades. Ambos atuam em ambientes sofisticados, com foco em drinks e experiência.

Plataforma diferente no serviço, mas que atende o mesmo mercado:
O BierPaulii atende o mesmo público em eventos descontraídos, mas de maneira diferente — focado em cervejas e cervejarias.

Plataforma mais interessante para a equipe:
O Makr Shakr é considerado a plataforma mais inspiradora. Apesar da sua complexidade, ele demonstra como um robô pode transformar o preparo de bebidas em uma experiência visual e funcional. No entanto, o Vesper se destaca por buscar um equilíbrio entre tecnologia acessível, segurança e estética adaptada a ambientes de médio porte. Ele mantém uma proposta mais contida, segura e funcional, sem deixar de lado a interação amigável e o apelo visual.

## Design

O Vesper foi projetado como um robô bartender fixo, com foco em acessibilidade, segurança e clareza funcional. Seu visual é limpo e simétrico, pensado para ser eficiente na entrega de bebidas e amigável na interação com o usuário.

 

Estrutura física e formas primitivas

O robô é inteiramente composto por formas geométricas simples, facilitando a modelagem e a produção:

9 retângulos:

1 base superior (estrutura dos braços)

1 base inferior (estrutura principal do robô)

1 para o tablet fixado na parte frontal inferior

2 bases das garras (esquerda e direita)

4 “dedos” retangulares (dois em cada garra)

8 cilindros:

2 braços (esquerdo e direito)

2 antebraços (esquerdo e direito)

4 alto-falantes cilíndricos (um em cada canto da base superior)

Essa combinação de caixas e cilindros permite um design modular, fácil de montar e adaptar para ambientes reais ou simulações digitais (URDF, Gazebo).
<!-- ![Partes do robô](Formato_Vesper.png) -->
<!-- ![Robô](Vesper_model.png) -->
<!-- ![Robôs](Vesper_model_color.png) -->
<img alt="Partes do robô" src="Formato_Vesper.png" height="200"/>
<img alt="Robô" src="Vesper_model.png" height="200"/>
<img alt="Robôs" src="Vesper_model_color.png" height="200"/>

## Ações do robô
O robô bartender Vesper realiza um conjunto de ações pré-programadas com foco em segurança, automação de preparo de bebidas e interação com o usuário. Abaixo, listamos as principais ações, seus pré-requisitos e os efeitos esperados no ambiente.

Ação: Ativação do robô (início da interação)

Descrição: O Vesper sai do modo de espera e inicia a interação ao detectar o toque do usuário no tablet frontal.

Pré-requisitos:

Tablet conectado e funcional.

Detecção de toque (input inicial do usuário).

Modificações esperadas no ambiente:

Início de reprodução de mensagens verbais.

Interface de menu é exibida no tablet.


Ação: Coleta e preparo da bebida

Descrição: O Vesper inicia a preparação da bebida solicitada, movendo internamente o braço para acessar reservatórios e dosar o conteúdo.

Pré-requisitos:

Pedido confirmado no tablet.

Ingredientes disponíveis (verificados por sensores internos).

Nenhum erro de sistema ou falha de segurança.

Modificações esperadas no ambiente:

Movimento visível do braço dentro da área de segurança.

Som ambiente do robô em funcionamento.

Copo pronto é posicionado na garra de entrega.

 

Ação: Entrega da bebida

Descrição: O braço do robô se estende para frente e posiciona o copo em uma zona acessível ao usuário, dentro da área segura e delimitada pela cortina.

Pré-requisitos:

Preparo da bebida finalizado com sucesso.

Espaço livre na área de entrega (sem obstruções).

Modificações esperadas no ambiente:

Luz de “bebida pronta” ativada.

Mensagem verbal: “Pegue com cuidado dos meus dedos, pode escorregar!”

Braço posicionado para retirada do copo.

Presença do copo visível para o cliente.

 

Ação: Retorno ao estado inicial

Descrição: Após a retirada da bebida, o robô retorna o braço para a posição de repouso e volta ao modo de espera.

Pré-requisitos:

Copo detectado como retirado (via sensor ou cronômetro interno).

Nenhuma solicitação de pedido em andamento.

Modificações esperadas no ambiente:

Luzes desligadas ou com brilho reduzido (indicando estado inativo).

Braço retraído e movimento cessado.

Sistema de voz em silêncio.

Tablet exibe novamente a tela de boas-vindas.

## Interações do robô

10 – Interações do Robô
O Vesper foi projetado para oferecer interações simples, claras e seguras. Suas interações são limitadas por sua estrutura fixa e pela cortina de segurança, mas ainda assim proporcionam uma experiência marcante ao usuário.

Interações Espaciais
Interação: Estender o braço com a bebida até o ponto de retirada

Descrição: O braço robótico do Vesper se move de dentro da cortina de segurança até a borda da zona acessível, estendendo a bebida ao usuário.

Pré-requisitos:

Pedido concluído no tablet.

Bebida preparada e posicionada corretamente.

Área de entrega livre de obstáculos.

Resposta emocional esperada:

Surpresa positiva pela precisão do gesto.

Confiança na operação do robô.

Sensação de cuidado, já que o robô respeita o espaço pessoal do usuário.

 

Interação: Iluminação do estado do robô (LEDs)

Descrição: O robô altera sua iluminação para indicar diferentes estados (em espera, preparando, bebida pronta).

Pré-requisitos:

Robô energizado e com LEDs operacionais.

Estado interno de operação alterado.

Resposta emocional esperada:

Clareza e compreensão do que está acontecendo.

Tranquilidade por entender que o robô está em funcionamento normal.

 

Obs.: O Vesper não realiza deslocamentos, por isso as interações espaciais são intencionalmente limitadas.

 

Interações Verbais
Interação: Saudação ao tocar no tablet

Descrição: Quando o usuário toca o tablet, o Vesper diz “Sejam bem-vindos!” e inicia a interação.

Pré-requisitos:

Toque detectado no tablet.

Sistema de áudio operacional.

Resposta emocional esperada:

Acolhimento e conforto.

Curiosidade e simpatia.

 

Interação: Orientação durante o pedido

Descrição: Durante o uso do tablet, o Vesper guia o usuário com frases como “Por favor selecione no tablet abaixo a sua bebida” e “Depois só esperar que vou começar o preparo”.

Pré-requisitos:

Usuário navegando no menu de bebidas.

Resposta emocional esperada:

Segurança na tomada de decisão.

Satisfação por receber instruções claras.

 

Interação: Aviso de bebida pronta

Descrição: Após finalizar o preparo, o Vesper anuncia “Bebida pronta! Pegue com cuidado dos meus dedos, pode escorregar!”

Pré-requisitos:

Preparo concluído.

Braço posicionado para entrega.

Resposta emocional esperada:

Senso de humor leve e agradável.

Entusiasmo por estar sendo atendido.

 

Interação: Despedida

Descrição: Após a retirada da bebida, o Vesper conclui: “Espero que tenha gostado! Obrigado e volte sempre!”

Pré-requisitos:

Detecção de retirada do copo (por tempo ou sensor).

Resposta emocional esperada:

Satisfação.

Encerramento amigável da experiência.

 

Interações Não-verbais
Interação: Movimento suave do braço

Descrição: O braço robótico do Vesper realiza movimentos lentos e previsíveis ao entregar o copo.

Pré-requisitos:

Pedido finalizado.

Sem obstáculos.

Resposta emocional esperada:

Tranquilidade e segurança.

Impressão de cuidado e respeito.

 

Interação: Mudança na postura da “garra” (dedos)

Descrição: Os dedos mecânicos simulam uma pegada cuidadosa no copo, reforçando o cuidado na entrega.

Pré-requisitos:

Copo preenchido e pronto.

Resposta emocional esperada:

Atenção ao detalhe.

Empatia com o robô (o gesto simula um cuidado humano).


[^1]: Fonte: Adaptado de <https://hazeshift.com.br/mapa-de-empatia/>
