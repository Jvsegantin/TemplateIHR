# **Vesper:** Robô Bartender

Trabalho de Interação Humano-Robô (IHR) apresentado ao Centro Universitário [FEI](https://portal.fei.edu.br/), como parte dos requisitos necessários para aprovação na disciplina de Interação Humano-Robô (IHR) (CCR230) do curso de Engenharia de Robôs, orientado pelo Prof. Dr. [Fagner de Assis Moura Pimentel](https://github.com/fagnerpimentel).

### Componentes do Grupo

- João Victor de Assis Segantin

### Resumo

O robô Vesper é um bartender automatizado desenvolvido para operar em restaurantes de padrão médio-alto com perfil tecnológico. Ele é responsável pela preparação e distribuição de bebidas diretamente no balcão do bar, onde os próprios clientes se dirigem para realizar seus pedidos. O Vesper atua de forma fixa, com braços robóticos responsáveis pela manipulação precisa dos insumos e preparo das bebidas. Sua aplicação visa otimizar o tempo de atendimento, reduzir a carga de trabalho dos garçons e garantir padronização e agilidade na entrega dos pedidos. Além disso, o robô conta com interação verbal por meio de alto-falantes e elementos de interação não verbal e espacial, promovendo uma experiência moderna e envolvente para os clientes.

### Introdução

A automação tem se consolidado como uma das principais tendências para enfrentar os desafios operacionais em diversos setores da economia, especialmente naqueles em que a agilidade e a eficiência no atendimento são fatores críticos para a satisfação do cliente. No setor gastronômico, restaurantes de médio a alto padrão têm buscado formas de incorporar tecnologias que agreguem valor à experiência dos frequentadores sem comprometer a qualidade do serviço humano. Um dos principais gargalos identificados nesse contexto é o atendimento em bares, onde a preparação e a entrega de bebidas durante horários de pico podem gerar filas, atrasos e sobrecarga dos garçons.

A proposta de robôs bartenders emerge como uma solução estratégica e inovadora diante dessa realidade. Além de aliviar a carga de trabalho da equipe humana, esses sistemas automatizados contribuem para a padronização das bebidas, reduzem falhas humanas e proporcionam uma experiência diferenciada ao cliente, alinhada às expectativas de um público cada vez mais conectado com soluções tecnológicas.

Neste cenário, foi desenvolvido o Vesper, um robô bartender fixo, projetado para operar em um bar dentro de um restaurante tecnologicamente sofisticado. O Vesper é responsável por receber os pedidos de bebidas diretamente dos clientes, preparar e entregá-las de maneira precisa e eficiente. Equipado com braços robóticos, sensores, saídas de áudio para interação verbal e cortinas de segurança para proteção dos usuários, ele representa uma fusão entre funcionalidade e design. Apesar de ser uma estação fixa, sua interação é pensada para transmitir simpatia e modernidade, sem causar estranhamento ao público.

### Publico Alvo

O robô bartender Vesper foi desenvolvido para atender um público que frequenta restaurantes de padrão médio-alto, em ambientes onde a tecnologia e a sofisticação fazem parte da proposta de valor do estabelecimento. Esse público busca agilidade no atendimento, praticidade no processo de pedidos e, ao mesmo tempo, experiências diferenciadas e inovadoras. Além disso, o Vesper também interage com os colaboradores do restaurante, principalmente os garçons responsáveis pelo suporte logístico da operação.

### Personas
Persona Primária – Cliente do restaurante
Nome: Carolina
Idade: 34 anos
Profissão: Designer de interiores
Contexto social e econômico: Classe média-alta, frequenta restaurantes premium e valoriza experiências gastronômicas inovadoras. Está conectada às tendências tecnológicas e busca ambientes que combinem conforto, estilo e praticidade.
Cultura e comportamento: Gosta de tirar fotos e compartilhar experiências nas redes sociais. Valoriza atendimento ágil e tem baixa tolerância a longas esperas.

O que o robô precisa saber antes de iniciar a tarefa:

O tipo de bebida desejada (menu com opções claras)

Restrições (como opção sem álcool ou alergias)

Confirmação de idade, para validar legalmente a entrega de bebidas alcoólicas

Persona Secundária – Garçom reabastecedor
Nome: Diego
Idade: 27 anos
Profissão: Garçom
Contexto social e econômico: Jovem trabalhador da área de serviços, com ensino médio completo e experiência em atendimento ao público. Trabalha em um restaurante de alto padrão onde eficiência e organização são essenciais.
Cultura e comportamento: Preza por praticidade, clareza nas tarefas e bom ambiente de trabalho. Está habituado a lidar com sistemas digitais e alertas operacionais.

O que o robô precisa saber antes de iniciar a tarefa:

Se os insumos estão no nível adequado (o próprio robô detecta e envia alertas)

Qual item está faltando ou precisa de reposição (ex: gelo, bebida alcoólica, copos)

Local de armazenamento para facilitar o reabastecimento

Outras personas
Gestores do restaurante: Avaliam o desempenho do robô em termos de custo-benefício, eficiência no atendimento e feedback dos clientes.

Técnicos de manutenção: Responsáveis por garantir o funcionamento contínuo do robô, atualizando software e monitorando o hardware.

Personas que não devem interagir com o robô
Crianças e adolescentes (menores de 18 anos):
Como o Vesper é projetado para servir bebidas alcoólicas, sua interação com menores de idade é estritamente proibida. Medidas preventivas devem ser tomadas, como bloqueios físicos, cortinas de segurança e futuros mecanismos de verificação de idade, para garantir a operação ética e segura do sistema.

### Mapa de empatia

![Mapa de empatia](empatia.png)

### Persona Primária: Rafael, 28 anos, publicitário
# O que ele PENSA E SENTE?
Rafael se sente empolgado com a experiência de um robô no ambiente de lazer. Quer diversão com eficiência e um toque de inovação. Sente-se seguro e curioso com o robô entregando bebidas. Espera uma interação amigável e tranquila.

# O que ele ESCUTA?
Conversas animadas entre amigos sobre o robô. Sons ambientes do bar, música moderna. Influenciadores nas redes comentando sobre “o bar do robô”.

# O que ele VÊ?
Ambiente iluminado, moderno, com pessoas socializando, luzes e o Vesper se movimentando com suavidade. Observa outros interagindo com o robô de forma positiva.

# O que ele FALA E FAZ?
Comenta com amigos sobre a inovação. Tira fotos e vídeos do robô. Pode acenar ou se aproximar, mantendo uma distância confortável e respeitosa. Ri ou faz comentários sobre “estar no futuro”.

# DOR:
Esperar muito tempo pelo atendimento. Sentir que o robô é brusco ou ameaçador. Não entender como funciona a interação.

# GANHOS:
Atendimento divertido, automatizado, rápido e seguro. Experiência diferenciada e memorável. Praticidade no recebimento da bebida.

### Persona Secundária: João, 40 anos, garçom
# O que ele PENSA E SENTE?
João vê o robô como uma ferramenta de apoio. Sente-se mais eficiente com o uso do Vesper, mas também carrega a responsabilidade de manter o robô abastecido e funcionando. Quer evitar erros ou falhas operacionais.

# O que ele ESCUTA?
Instruções da equipe técnica ou do supervisor. Feedback dos colegas sobre o funcionamento do robô. Clientes comentando sobre a experiência com curiosidade e entusiasmo.

# O que ele VÊ?
A base operacional do robô, com reservatórios e compartimentos de bebida. O fluxo de pessoas no salão e as rotas do robô em operação. Painéis de status ou sinais visuais no Vesper indicando necessidades.

# O que ele FALA E FAZ?
Reabastece compartimentos, faz verificações rápidas, limpa sensores ou superfície quando necessário. Comenta entre colegas sobre a praticidade ou os desafios. Relata qualquer problema ao suporte técnico.

# DOR:
Atrasos no reabastecimento, mau funcionamento ou dúvidas técnicas. Dificuldade de acesso ao compartimento do robô. Falta de treinamento adequado.

# GANHOS:
Redução de esforço físico, agilidade no atendimento. Mais tempo para focar em outras demandas. Reconhecimento por trabalhar em um ambiente moderno.

### Contexto de uso
# Ambiente de interação:
O Vesper opera em ambientes sociais fechados como bares temáticos, lounges modernos, feiras tecnológicas, eventos corporativos ou ambientes universitários voltados à inovação. O espaço possui fluxo moderado de pessoas, iluminação controlada, mesas distribuídas com corredores largos o suficiente para permitir a movimentação segura do robô. Há uma área reservada para reabastecimento supervisionada por funcionários.

# Contexto social, econômico e cultural:
O ambiente é composto majoritariamente por adultos jovens e profissionais de classe média urbana, com interesse por tecnologia, inovação e experiências diferenciadas. Culturalmente, trata-se de um público habituado a novidades digitais, que consome conteúdo em redes sociais e valoriza serviços automatizados. O uso do robô agrega um diferencial futurista ao local e reforça o posicionamento da marca como inovadora.

# Informações que o robô deve saber antes de iniciar a tarefa:

# Mapeamento do ambiente: 
Localização das mesas, pontos de recarga, rota segura de circulação, áreas de restrição (como zonas com crianças).

# Controle de volume:
 Adequação do nível dos speakers ao ambiente (evitando sons altos em locais mais silenciosos ou ao se aproximar dos clientes).

# Presença de obstáculos: 
Localização de objetos fora do lugar, acúmulo de pessoas ou móveis que interfiram na rota.

# Nível de bebida no compartimento:
Evitar iniciar entregas com estoque insuficiente.

# Identificação de zonas proibidas: 
O robô deve reconhecer áreas onde sua presença não é recomendada, como mesas infantis, pistas de dança ou corredores estreitos.

# Estado do ambiente: 
Nível de iluminação, se há som ambiente alto, clima (para adaptar eventuais mensagens ou tom de voz).


### Jornada do usuário

- Criar uma narrativa para o o seu robô e o usuário.
- Determine o passo a passo que o usuário realiza desde o primeiro até o último encontro com robô na realização da tarefa.
- O que está acontecendo com o ambiente quando o robô está interagindo com o usuário?
  - Descreva o que acontece ou pode acontecer passo a passo
  - Como a tarefa começa? Como a tarefa evolui? Como a tarefa termina?
- Enfatize todos os momentos em que acontece uma interação verbal, não-verbal e espacial.

## Análise de concorrência

- Pesquise robôs existentes atualmente que possam fazer a tarefa deste projeto.
- Selecione pelo menos 3 robôs diferentes que podem fazer essa tarefa.
- Em relação aos concorrentes, respondam as seguintes perguntas?
  - Existe plataforma similar que atende o mesmo mercado e funcionalidades? Se sim: Quais os pontos positivos? Quais os pontos negativos?
  - Existe plataforma diferente quanto ao serviço, mas que atenda esse mercado? Se sim: Quais os pontos positivos? Quais os pontos negativos?
  - Quais plataformas sua equipe acha mais interessantes? Qual a justificativa?

## Design

- Pense nas características de Affordances do seu robô. Que tipo de acessibilidades devem ser consideradas dentro do seu projeto?
- Discuta o papel das expectativas do usuário no projeto de um robô. Qual a importância e pontos a serem considerados se você quiser vender esse robô  seu robô?
- O seu robô tem um padrão com mais ou menos características antropomórficas? Qual padrão é mais aceito pela sociedade dentro do projeto que você está desenvolvendo?
- Quais o design mais apropriado para o robô deste projeto? Modele o seu robô com desenhos de formas primitivas (caixas, cilindros, esferas)

<!-- ![Partes do robô](partes_do_robo.png) -->
<!-- ![Robô](robo.png) -->
<img alt="Partes do robô" src="partes_do_robo.png" height="200"/>
<img alt="Robô" src="robo.png" height="200"/>

## Ações do robô

- Para cada ação:
  - Descreva a ação.
  - Determine os pré-requisitos para que a ação aconteça
  - Determine o que se espera que seja modificado no ambiente quando a ação é finalizada

## Interações do robô

### Espacial

- Para cada interação:
  - Descreva a interação.
  - Determine os pré-requisitos para que a interação aconteça
  - Determine espera de resposta emocional do usúario quando a interação é finalizada

### Verbal

- Para cada interação:
  - Descreva a interação.
  - Determine os pré-requisitos para que a interação aconteça
  - Determine espera de resposta emocional do usúario quando a interação é finalizada

### Não-verbal

- Para cada interação:
  - Descreva a interação.
  - Determine os pré-requisitos para que a interação aconteça
  - Determine espera de resposta emocional do usúario quando a interação é finalizada

[^1]: Fonte: Adaptado de <https://hazeshift.com.br/mapa-de-empatia/>

<!-- TODOs:
- Add exemplos
 -->
