raw_data_input = File.read("part1.dat").chomp

class Solver
  def initialize(raw_data_input)
    @number_ranges = []
    for raw_number_range_list in raw_data_input.split(',')
      # split 1-2 -> [1,2]
      number_range = raw_number_range_list.split('-').map(&:to_i)
      number_range_start = number_range [0]
      number_range_end = number_range [1]
      # convert string to number
      # convert it to hashtable {start:1, end:2}
      @number_ranges.push({ start: number_range_start, end: number_range_end })
    end
    @invalid_numbers = 0
  end

  def process_number(number)
    number_string = number.to_s
    if number_string.length.odd?
      return
    end
    half = number_string.length / 2

    first_half  = number_string[0...half]
    second_half = number_string[half..]

    if first_half == second_half
      @invalid_numbers += number
    end
  end

  def solve
    for number_range in @number_ranges
        for i in number_range[:start]..number_range[:end]
          process_number(i)
        end
    end
    pp @invalid_numbers
  end

end

solver = Solver.new(raw_data_input)
solver.solve
