# Atividade – Prompt Mestre em Programação de Computadores
 
## Tema: Lógica de Programação Básica: Criando um Radar de Velocidade (Estruturas Condicionais If/Else).

### Prompt Mestre Inicial 
"Escreva um código para um radar de trânsito."

### Variação 1 
"Sou iniciante em programação e estou aprendendo lógica.
Explique como funciona a estrutura 'IF/ELSE' (Se/Senão) usando um exemplo prático de um carro passando por um radar de velocidade na rodovia. Não use código ainda, me explique apenas a lógica como se estivesse desenhando em um quadro."
**Resposta do LLM: Imagine um radar de velocidade em uma rodovia. O limite da via é 80 km/h. Quando um carro passa, o computador dentro do radar precisa tomar um decisão rápida. Para isso, ele usa a estrutura SE/SENÃO (que em inglês chamamos de IF/ELSE).** 

### Variação 2
"Agora, transforme essa lógica do radar em um código simples em Python. Por favor, coloque comentários linha por linha explicando o que cada variável e símbolo faz, para que um estudante do primeiro semestre consiga ler e entender sozinho."
**Resposta do LLM: Passo 1 (Guardando os dados): O computador precisa criar duas "caixinhas" na sua memória. Na primeira caixinha, ele guarda o Limite da Via (ex: 80). Na segunda caixinha, ele guarda a Velocidade do Carro que o sensor acabou de medir (ex: 90). Passo 2 (A Condição - O 'SE'): Aqui entra a tomada de decisão. Nós mandamos o computador comparar as duas caixinhas com a seguinte regra: SE a [Velocidade do Carro] for MAIOR que o [Limite da Via]... Passo 3 (O resultado verdadeiro): ...ENTÃO, se essa afirmação for verdade, execute a ação: "Emitir a notificação de Veículo Multado". Passo 4 (O caminho alternativo - O 'SENÃO'): ...SENÃO, se a afirmação for mentira (o carro estava a 80 ou menos), ignore a multa e execute a ação: "Emitir a mensagem de Boa Viagem".**

### Variação 3
"O código funcionou bem, mas no mundo real os radares costumam ter uma tolerância antes de multar o motoristam. Como eu altero esse código em Python para que o carro só seja multado se passar 10% acima do limite da via? Me explique a matemática que você usou para atualizar o código."
**Resposta da LLM: A Matemática: O computador ainda sabe que o Limite da Via é 80. Mas agora, nós mandamos ele fazer uma conta: pegar esse limite e adicionar 10% de "gordura". Matematicamente, se multiplicarmos 80 por 1,10, o resultado é 88.
A Nova Caixinha: O computador pega esse resultado (88) e guarda em uma terceira caixinha chamada Limite com Tolerância.
A Nova Decisão: A grande sacada acontece agora. A nossa regra principal muda. O radar não vai mais comparar o carro com a placa de 80. Ele vai perguntar: SE a [Velocidade do Carro] for MAIOR que o [Limite com Tolerância]...**

### Reflexão 
A qualidade e tempo de resposta que a IA depende totalmente do nível de detalhe do nosso comando. Quando pedi apenas o código inicial, recebi uma resposta engessada, mas ao exigir analogias e o passo a passo lógico, a ferramenta se transformou em uma tutora particula. Para o meu momento atual de aprendizado, a versão focada na lógica estruturada sem código (Versões 2 e 3) foi disparada a mais útil, pois me forçou a entender a tomada de decisão do computador antes de me preocupar com regras de sintaxe. No mundo real, pretendo usar essa técnica de refino de prompts para desconstruir problemas passo a passo, caso eu crie um script complexo de regras de trânsito e multas para um servidor de roleplay, por exemplo, usarei a IA primeiro para mapear e validar todas as condições matemáticas no papel, garantindo que a base lógica esteja perfeita antes de digitar a primeira linha de código no computador. 
