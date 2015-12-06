function [Norms,starts,ends] = SeperateNormsFixed(normals, faces, vertices)
%initialize Norms to how many normals exist
 Norms(:,:) = zeros(size(normals));

%Load closeNorms with normals faces and areas
for i = 1 : size(normals);
    Norms(i,1:3) = normals(i,1:3);
    Norms(i,4:6) = faces(i,1:3);
    Norms(i,7) = getAreaActual((Norms(i,4:6)),vertices);
end;


%Make vectors for display
starts = zeros(size(normals));
ends = Norms(:,1:3);

%Weight closeNorms based on area
for q = 1 : size(normals)
    ends(q,:) =  ends(q,:) .* Norms(q,7);
end

%Display vectors
quiver3(starts(:,1), starts(:,2), starts(:,3), ends(:,1), ends(:,2), ends(:,3));
axis equal
    