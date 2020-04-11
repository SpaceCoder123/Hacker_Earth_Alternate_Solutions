function [] = Image_Rotation(n,A)

Resultant=[];

if n==length(A)
    for i=1:length(A)
        %disp(i)
        for j=1:length(A)
            %disp(j)
            x=(n+1)-j;
            Resultant(i,j)=A(x,i);
        end
    end
end
disp(Resultant)  
end

