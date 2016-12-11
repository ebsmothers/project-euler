function solution = ProjectEuler12(k)
for n = 1:50000
    triangular = n*(n+1)/2;
    if(numdivisors(triangular) > k)
        solution = triangular;
        return
    end
end;