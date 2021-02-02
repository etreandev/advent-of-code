
function fibtop()

    x1::UInt128 = 1
    x2::UInt128 = 1

    function closuredfib()
        x3::UInt128 = x1 + x2
        println(x3)
        (x1, x2) = (x2, x3)
        end

end

f = fibtop()

for num in 1:100
    f()
end
