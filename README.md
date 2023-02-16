para ver o codigo funcionando seguindo o conceito de exclusão mutua, siga as seguintes instruções:


Abra um terminal e execute o arquivo Server.py

Agora abra pelo menos dois terminais e execute o arquivo cliente.py

  "Você pode executar o arquivo cliente.py em quantos terminais você quiser. cada véz que você executa o arquivo cliente.py, isso cria uma conexão que será recebida pelo socket"
 
 
  "Você deve executar os clientes quase que ao mesmo tempo.
  Quando você executa o cliente, o socket irá esperar até que o cliente mande alguma coisa para ele.
  Então digite sua conta e quanto deseja sacar, em ambos os clientes. 
  Após isso aperte enter em ambos os clientes"
  
 Isso irá criar threads com diferentes processos que irão concorrer para serem execultados. Mas usando o algoritimo de exclusão mutua, controlamos para que um processo não seja execultado enquanto o outro está consumindo recurso
  
