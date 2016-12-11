i=1;
a=1;
b=2;
c=0;

while c < 4000000
    c = a+b;
    a = b;
    b = c;
    i = i+1;
end

fibonacci = zeros(1,i);
fibonacci(1) = 1;
fibonacci(2) = 2;

for j = 3:i
fibonacci(j) = fibonacci(j-1) + fibonacci(j-2);
end

ans = 0;
for k = 1:11
    ans = ans + fibonacci(3*k-1)
end
    
