lines = File.readlines("part2.dat").map{ |item| item.chomp }

class Solver
  def initialize(raw_operatin_array)
    @operations = []
    for operation in raw_operatin_array do
      operation_symbol = operation[0]
      operation[0] = ''
      operation_number = operation.to_i

      @operations.push({operation_symbol: operation_symbol, operation_number: operation_number})
    end
    @has_hit_0 = 0
    @password = 50
  end

  def solve
    for operation in @operations
      operation[:operation_number].times do

        case operation[:operation_symbol]
        when 'L'
          @password -= 1
        when 'R'
          @password += 1
        end
        @password %= 100
        @has_hit_0 += 1 if @password.zero?
      end
    end
    p @has_hit_0
  end
end

solver = Solver.new(lines)
solver.solve
