for a = 1:500
    for b=1:499
        c = 1000 - a - b;
        if(istriple(a,b,c)==1)
            solution = a*b*c;
        end
    end
end