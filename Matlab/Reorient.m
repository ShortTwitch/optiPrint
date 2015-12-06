function [verts] = Reorient(verts, flips)
    if flips(1) > 0
        for i = 1:length(verts) %rotate around x
            y = verts(i,2);
            z = verts(i,3);
            verts(i,2) = y*cos((pi/180)*flips(1)) - z*sin((pi/180)*flips(1));
            verts(i,3) = y*sin((pi/180)*flips(1)) + z*cos((pi/180)*flips(1));
        end
    end;
    if flips(2) > 0 %rotate around y
        for i = 1:length(verts)
            x = verts(i,1);
            z = verts(i,3);
            verts(i,1) = x*cos((pi/180)*flips(2)) - z*sin((pi/180)*flips(2));
            verts(i,3) = x*sin((pi/180)*flips(2)) + z*cos((pi/180)*flips(2));
        end
    end;
    if flips(3) > 0 %rotate around z
        for i = 1:length(verts)
            x = verts(i,1);
            y = verts(i,2);
            verts(i,1) = x*cos((pi/180)*flips(3)) - y*sin((pi/180)*flips(3));
            verts(i,2) = x*sin((pi/180)*flips(3)) + y*cos((pi/180)*flips(3));
        end
    end;
end