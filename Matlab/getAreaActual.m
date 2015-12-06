function [area] = getAreaActual (faces, vertices)
 %   [P] = [vertices(faces(1,1),1:3) vertices(faces(1,2),1:3) vertices(faces(1,3),1:3)];
 %   % Length of edges
 %   L=[sqrt(sum((P(1,:)-P(2,:)).^2)) sqrt(sum((P(2,:)-P(3,:)).^2)) sqrt(sum((P(3,:)-P(1,:)).^2))];
    
 %   % Area calculation with Heron's formula
 %   s = ((L(1)+L(2)+L(3))/2); 
 %   area = sqrt(s*(s-L(1))*(s-L(2))*(s-L(3)));

%  [P] = [vertices(octants(j,1,i),:); vertices(octants(j,2,i),:); vertices(octants(j,3,i),:)];
% 
%  % Length of edges
%  L=[sqrt(sum((P(1,:)-P(2,:)).^2)) sqrt(sum((P(2,:)-P(3,:)).^2)) sqrt(sum((P(3,:)-P(1,:)).^2))];
% 
%  % Area calculation with Heron's formula
%  s = ((L(1)+L(2)+L(3))/2); 
%  area = sqrt(s*(s-L(1))*(s-L(2))*(s-L(3)));

P = [vertices(faces(1,1),1:3); vertices(faces(1,2),1:3); vertices(faces(1,3),1:3)];
%Length of edges
 L=[sqrt(sum((P(1,:)-P(2,:)).^2)) sqrt(sum((P(2,:)-P(3,:)).^2)) sqrt(sum((P(3,:)-P(1,:)).^2))];

 % Area calculation with Heron's formula
 s = ((L(1)+L(2)+L(3))/2); 
 area = sqrt(s*(s-L(1))*(s-L(2))*(s-L(3)));