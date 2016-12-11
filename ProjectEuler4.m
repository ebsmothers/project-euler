ans = 0;

Product = zeros(100);

for i = 900:999
    for j = 900:999
        Product(i-899,j-899) = i * j;
    end
end

Palindrome = [];
for i = 810000:999999
    if IsPalindrome(i) == 1
        Palindrome(i) = i;
    end
end

Intersect = intersect(Product,Palindrome);
        