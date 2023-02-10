data = open("../input/day-03.txt") do file
    read(file, String)
end

data = split(data, "\r\n")
data = data[1:end-1]



function SlideTop(IncremX::Integer, IncremY::Integer, data::AbstractArray)
    x = 1
    y = 1
    numTrees = 0
    ld = length(data[1])
    function Slider()
        x += IncremX
        y += IncremY
        y > ld ? y %= ld : y = y
        numTrees += data[x][y] == "#"[1] ? 1 : 0

        return (numTrees, x)
    end
end

S = SlideTop(1, 3, data)
x = 0
while x < length(data)
    (numTrees, x) = S()
end
println(numTrees)

# Part two

Slides = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
Prod = 1
for slide in Slides
    S = SlideTop(slide[2], slide[1], data)
    x = 0
    while x < length(data)
        (numTrees, x) = S()
    end
    Prod *= numTrees
end
println(Prod)
