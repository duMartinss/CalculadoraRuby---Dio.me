array = []
puts 'Insira 3 numeros'
puts 'Numero um: '
array.push gets.chomp.to_i
puts 'Numero dois: '
array.push gets.chomp.to_i
puts 'Numero tres: '
array.push gets.chomp.to_i

conta = array[0] * array[1] * array[2]
puts "Resultado é [#{conta}]"
