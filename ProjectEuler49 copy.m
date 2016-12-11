function [ ans ] = ProjectEuler49()
% Find an arithmetic sequence of four digit numbers that are all prime and
% permutations of one another and concatenate them

% for n = 1000:9999
%     permvec = findperm(n)
% 
% end
findperm(1567)
function[permvec] = findperm(n)
nvec = sscanf(sprintf('%u',n),'%1d');
permvec = perms(nvec);
end


end

