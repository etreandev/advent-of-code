cd("C:/Users/Lenovo/OneDrive/Documentos/CodeChallenges/AdventOfCode2020")
data = open("input_day4.txt") do file
    read(file, String)
end

using Pipe

#=
data = """
eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007"""
=#
data = split(data[1:end-2], "\r\n\r\n")
#data = split(data, r"(\n\n|\n)")

SplitPassport(S::AbstractString) = split(S, r"(\r\n| )")
GetUniqueFields(PInfo::AbstractArray) = [split(item, ":")[1] for item in PInfo]

function CheckNumberOfFields(Fields::AbstractArray)
    MandatoryFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    sum([item in Fields for item in MandatoryFields])
end

IsValid(PInfo::AbstractString) = @pipe PInfo |>
    SplitPassport |>
    GetUniqueFields |>
    CheckNumberOfFields  |>
    ==(_, 7)

sum([IsValid(item) for item in data])

# Define InBetween
function InBetween(Min::Integer, Max::Integer, Num::AbstractString)
    INum = parse(Int16, Num)
    return Min <= INum & INum <= Max
end

function IsHeightValid(Height::AbstractString)
    m = match(r"(?<Height>\d+)(?<Units>(in|cm))$", Height)
    isnothing(m) && return false
    m[:Units] == "in" && return InBetween(59, 76, m[:Height])
    m[:Units] == "cm" && return InBetween(150, 193, m[:Height])
end

# Create test Battery.
InfoDict = Dict([
    ("byr", (Year) -> @pipe match(r"\d{4}", Year::AbstractString) |>
                            !isnothing && return InBetween(1920, 2002, Year)),

    ("iyr", (Year) -> @pipe match(r"\d{4}", Year::AbstractString) |>
                            !isnothing && return InBetween(2010, 2020, Year)),

    ("eyr", (Year) -> @pipe match(r"\d{4}", Year::AbstractString) |>
                            !isnothing && return InBetween(2020, 2030, Year)),

    ("hgt", (Height) -> @pipe IsHeightValid(Height::AbstractString)),

    ("hcl", (Color) -> @pipe match(r"\#[a-f0-9]{6}", Color)  |> !isnothing),

    ("ecl", (Color) -> Color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),

    ("pid", (ID) -> @pipe match(r"^\d{9}$", ID) |> !isnothing),

    ("cid", (cid) -> true)
])

function CheckFields(PInfo::AbstractString, InfoDict::Dict)
    Info = PInfo |> SplitPassport

    for item in Info
        m = match(r"(?<Field>[a-z]{3}):(?<Value>.*)", item)
        InfoDict[m[:Field]](m[:Value]) || return false
    end
    return true
end

IsValid2(PInfo::AbstractString, InfoDict::Dict) = IsValid(PInfo) && CheckFields(PInfo, InfoDict)

sum([IsValid2(item, InfoDict) for item in data])
