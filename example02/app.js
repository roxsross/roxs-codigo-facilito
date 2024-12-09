const express = require('express');
const path = require('path');
const os = require('os');

const app = express();
app.set('view engine', 'ejs')
const PORT = process.env.PORT || 3000;

// Configuración para servir archivos estáticos desde la carpeta 'public'
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.render(
    'index',
    {
      ipv4: getIPv4Address()
    },
  );
});


app.listen(PORT, () => {
  console.log(`Servidor Node.js en ejecución en el puerto ${PORT}`);
});

const getIPv4Address = () => {
  const networkInterfaces = os.networkInterfaces();
  for (let iface of Object.values(networkInterfaces)) {
    for (let alias of iface) {
      if (alias.family === 'IPv4' && !alias.internal) {
        return alias.address;
      }
    }
  }
  return null;
}