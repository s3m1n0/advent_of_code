lines = File.readlines("part1.dat").map{ |item| item.chomp }


class Solver
  def initialize(raw_operatin_array)
    @operations = []
    for operation in raw_operatin_array do
      operation_symbol = operation[0]
      operation[0] = ''
      operation_number = operation.to_i
      operation_number = -operation_number if operation_symbol == 'L'

      @operations.push(operation_number)
    end
    @has_hit_exactly_0 = 0
    @password = 50
  end

  def solve
    for operation in @operations
      password = (@password + operation) % 100
      @has_hit_exactly_0 += 1 if password.zero?
      @password = password
    end
    puts "the solution is #{@has_hit_exactly_0}"
  end
end

solver = Solver.new(lines)
solver.solve
