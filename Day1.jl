data = open("input_day1.txt") do file
    read(file, String)
end
data = split(data, "\r\n")
data = data[1:end-1]

RunUpTo = (i, j) ->  i == j + 1 ? (i + 1, 1) : (i, j + 1)
ExtractParse = (Alist, i, j) ->  (parse(Int, Alist[i]), parse(Int, Alist[j]))

function CheckIfSums(TarSum::Int)
    (i, j) = (2, 1)

    function SumElementsFromList(List)
        (x1, x2) = ExtractParse(List, i, j)
        (i, j) = RunUpTo(i, j)
        return x1 + x2 == 2020 ? x1 * x2 : nothing
    end

end

Sum2020 = CheckIfSums(2020)


while flag
    x = Sum2020(data)
    flag = x == nothing ? true : false
end
println(x)



function RunUpTo3b(i, j, k)
    (j, k) = j == k + 1 ? (j + 1, 1) : (j, k + 1)
    (i, j) = i == j ? (i + 1, 2) : (i, j)
    k = j == 2 ? 1 : k
     return (i, j, k)
 end

ExtractParse3 = (Alist, i, j, k) ->  (parse(Int, Alist[i]), parse(Int, Alist[j]), parse(Int, Alist[k]))

function CheckIfSums3(TarSum::Int)
    (i, j, k) = (3, 2, 1)

    function SumElementsFromList3(List)
        (x1, x2, x3) = ExtractParse3(List, i, j, k)
        (i, j, k) = RunUpTo3b(i, j, k)
        return x1 + x2 + x3 == 2020 ? x1 * x2 * x3 : nothing
    end

end

Sum20203 = CheckIfSums3(2020)


while flag
    x = Sum20203(data)
    flag = x == nothing ? true : false
end
println(x)
