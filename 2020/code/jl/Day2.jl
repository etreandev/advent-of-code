data = open("../input/day-02.txt") do file
    read(file, String)
end
data = split(data, "\r\n")
data = data[1:end-1]

InBetween(A::Int64, B::Int64, x::Int64)  = (x >= A) & (x <= B) ? true : false
InBetween(A::AbstractString, B::AbstractString, x::Int64) = InBetween(parse(Int,A), parse(Int,B), x)


function AnalyzePassword(Pswd::AbstractString)
    m = match(r"(?<A>\d+)-(?<B>\d+) (?<letter>[a-z]+): (?<Password>[a-z]+)$", Pswd)

    r = Regex(m[:letter])
    c = length(collect(e.match for e in eachmatch(r, m[:Password])))

    return InBetween(String(m[:A]), String(m[:B]), c) ? true : false
end

Valids = [AnalyzePassword(Pswd) for Pswd in data]

println(sum(Valids))

GetLettersInPosition(A::Integer, B::Integer, Pswd::AbstractString) = (Pswd[A], Pswd[B])
function GetLettersInPosition(A::AbstractString,
                            B::AbstractString,
                            Pswd::AbstractString) 
    GetLettersInPosition(parse(Int,A), parse(Int,B), Pswd::AbstractString)
end


function AnalyzePassword2(Pswd::AbstractString)
    m = match(r"(?<A>\d+)-(?<B>\d+) (?<letter>[a-z]+): (?<Password>[a-z]+)$", Pswd)
    (l1, l2) = GetLettersInPosition(m[:A], m[:B], m[:Password])
    sum([l1==m[:letter][1], l2==m[:letter][1]]) == 1 ? 1 : 0
end

Valids2 = [AnalyzePassword2(Pswd) for Pswd in data]
sum(Valids2)
