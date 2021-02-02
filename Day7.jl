testdata = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

data = open("input_day7.txt") do file
    read(file, String)
end
using Pipe

ParseRules(data::AbstractString, delim::Regex) = @pipe data |>
            split(_, delim) |>
            _[1:end-1] |>
            match.(r"(?<Container>.*) bag([s]?) contain (?<Contents>.*)\.", _)]



function GetValidContainers(Content::AbstractString)
    Rules = ParseRules(data, r"\r\n")
    [item[:Container] for item in Rules if occursin(Content, item[:Contents])]
end


function FindContainers()
    Contents = ["shiny gold"]
        function GetContainers()
            NewContainers = []
            for item in Contents
                append!(NewContainers, GetValidContainers.(item))
            end

            length(NewContainers) > 0 && (Contents = NewContainers)
            return Contents
        end
end

GC = FindContainers()

i=1
Contents = []
while i < 1000
    append!(Contents, GC())
    i+=1
end

Contents = Set(Contents)

function ParseContents(Contents::SubString{String})
    Pattern = r"^(?<BagNo>\d)? (?<BagCo>.*) bag"
    m = @pipe Contents |> split(_, ", ") |> match.(Pattern, _)
end

function RulesToDict(Rules::Vector{RegexMatch})
    RulesDict = Dict{AbstractString, SubString{String}}(
        [(Rule[:Container], Rule[:Contents]) for Rule in Rules]
    )
end


function GetInnerContents(Rules::RegexMatch, SuperContainer::String)
    Containers = [SuperContainer]
    RulesDict = RulesToDict(Rules)

        function GetContents()
