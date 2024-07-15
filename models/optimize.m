z = peaks(25);
subplot(2,3,1);
mesh(z)

z = peaks(25);
subplot(2,3,2);
surf(z)

subplot(2,3,3);
surfl(z)
colormap(pink)    % change color map
shading interp    % interpolate colors across lines and faces
subplot(2,3,4);

contour(z,16)
colormap default    % change color map

subplot(2,3,5);

x = -2:.2:2;
y = -2:.25:2;
z = -2:.16:2;

[x,y,z] = meshgrid(x,y,z);
v = x.*exp(-x.^2-y.^2-z.^2);

xslice = [-1.2,.8,2];    % location of y-z planes
yslice = 2;              % location of x-z plane
zslice = [-2,0];         % location of x-y planes

slice(x,y,z,v,xslice,yslice,zslice)
xlabel('x')
ylabel('y')
zlabel('z')

subplot(2,3,6);
x = -2:.2:2; 
y = -1:.2:1;

[xx,yy] = meshgrid(x,y);
zz = xx.*exp(-xx.^2-yy.^2);
[px,py] = gradient(zz,.2,.2);

quiver(x,y,px,py)
xlim([-2.5 2.5])    % set limits of x axis