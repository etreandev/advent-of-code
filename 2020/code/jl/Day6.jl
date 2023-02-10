data = open("../input/day-06.txt") do file
    read(file, String)
end
#data = split(data, "\r\n")
#data = data[1:end-1]

using Pipe

SplitByGroups(data::String) = @pipe data |>
            split(_, r"(\n\n|\r\n\r\n)")  |>
            replace.(_, r"(\r|\n)" => "")

function CountUniqueAnswers(Answers::String)

    CurrentAnswers = ""
    for letter in Answers
        occursin(letter, CurrentAnswers) || (CurrentAnswers *= letter)
    end
    return length(CurrentAnswers)
end

CountUniqueAnswers.(SplitByGroups(data)) |> sum

# Second star.

function CountAllAnswers(GroupAnswers::AbstractString)
    IndividualAnswers = split(GroupAnswers, "\r\n")
    AnswerIntersection = IndividualAnswers[1]
    for Answer in IndividualAnswers[2:end]
        AnswerIntersection = intersect(AnswerIntersection, Answer)
    end
    return length(AnswerIntersection)
end

testdata = """abc\r\n\r\na\r\nb\r\nc\r\n\r\nab\r\nac\r\n\r\na\r\na\r\na\r\na\r\n\r\nb"""

[CountAllAnswers(GroupAnswer) for GroupAnswer in split(data[1:end-2], "\r\n\r\n")] |> sum
