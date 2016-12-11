function [ ans ] = ProjectEuler49()
% Find an arithmetic sequence of four digit numbers that are all prime and
% permutations of one another and concatenate them

for n = 1000:9999
    permvec = findperm(n);
    
    for i = 1:size(permvec,1)
        intpermvec(i) = sscanf(sprintf('%1d',permvec(i,:)),'%u');
    end
    
    % Fill difference array 
    diff = zeros(length(intpermvec));
    for i = 1:length(intpermvec)
        for j = 1:i-1
            if isprime(intpermvec(i)) & isprime(intpermvec(j))
                diff(i,j) = abs(intpermvec(i)-intpermvec(j));
            end
        end
    end
    diff = diff(diff ~= 0);
    
    
    % Search for repeats
    if thrice(diff)
        fprintf('%i\n',intpermvec)
    end
    
            
            
end

    function[permvec] = findperm(n)
    nvec = sscanf(sprintf('%u',n),'%1d');
    permvec = perms(nvec);
    permvec = unique(permvec,'rows');
    end

    function[isit] = thrice(diff)
    isit = false;
    y = zeros(size(diff));
    for i = 1:length(diff)
        y(i) = sum(diff == diff(i));
    end
    if max(y) >= 3
        isit = true;
    end
    end
    
end


