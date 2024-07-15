z=peaks(40);
subplot(2,3,1);
mesh(z);
subplot(2,3,2);
surf(z);
subplot(2,3,3);
meshc(z);
subplot(2,3,4);
surfc(z)
subplot(2,3,5);
meshz(z)

subplot(2,3,6);
x=(0:0.01:2*pi);
y=x;
[X,Y]=meshgrid(x,y);
z=cos(X)+sin(Y);
mesh(X,Y,z)
