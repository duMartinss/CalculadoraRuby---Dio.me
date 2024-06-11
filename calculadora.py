loop do
    puts 'Selecione uma das opções abaixo'
    puts '0 - Sair'
    puts '1 - Adição'
    puts '2 - Subtração'
    puts '3 - Multiplicação'
    puts '4 - Divisão'
    print 'Digite sua escolha: '

    escolha = gets.chomp.to_i

    if escolha == 1
        print 'Digite o primeiro numero: '
        primeiroA = gets.chomp.to_i
        print 'Digite o segundo numero: '
        segundoA = gets.chomp.to_i
        adicao = primeiroA + segundoA
        puts "O resultado será [#{adicao}]"
    elsif escolha == 2
        print 'Digite o primeiro numero: '
        primeiroS = gets.chomp.to_i
        print 'Digite o segundo numero: '
        segundoS = gets.chomp.to_i
        subtracao = primeiroS - segundoS
        puts "O resultado será [#{subtracao}]"
    elsif escolha == 3
        print 'Digite o primeiro numero: '
        primeiroM = gets.chomp.to_i
        print 'Digite o segundo numero: '
        segundoM = gets.chomp.to_i
        multiplicacao = primeiroM * segundoM
        puts "O resultado será [#{multiplicacao}]"
    elsif escolha == 4
        print 'Digite o primeiro numero: '
        primeiroD = gets.chomp.to_i
        print 'Digite o segundo numero: '
        segundoD = gets.chomp.to_i
        divisao = primeiroD % segundoD
        if divisao == 0
            divisao2 = primeiroD / segundoD
            puts "O resultado será [#{divisao2}]"
        else 
            puts "O resultado será [#{divisao}], o resultado não é exato"
        end 
    elsif escolha == 0
        break
    else
        resultado = 'Opção invalida'
        
    end
end
