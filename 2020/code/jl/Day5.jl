data = open("../input/day-05.txt") do file
    read(file, String)
end

using Pipe

function DecodeElement(Element::AbstractString)
    Codex = Dict{Char, Bool}(
        'F' => false,
        'B' => true,
        'L' => false,
        'R' => true
    )

    Pow = length(Element)
    DecodedElement = 0
    for letter in Element
        Pow -= 1
        Codex[letter] && (DecodedElement += 2^Pow)
    end
    return DecodedElement
end


function DecodeRowSeat(Ticket::AbstractString)
    m = match(r"(?<Row>[FB]{7})(?<Seat>[LR]{3})", Ticket)
    Row = DecodeElement(m[:Row])
    Seat = DecodeElement(m[:Seat])

    return Row *8 + Seat
end


maximum(DecodeRowSeat.(data))

# Second Star
DecSeats = DecodeRowSeat.(data)

minimum(DecSeats)

[item for item in minimum(DecSeats):maximum(DecSeats) if item ∉ DecSeats][1]
