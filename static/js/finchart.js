const fin = document.getElementById('finchart');

new Chart(fin, {
  type: 'bar',
  data: {
    labels: ['Pochampally', 'Venkatagiri', 'Khadi', 'Baluchari', 'Lenin', 'Brocade', 'Boho Pots', 'Bangles', 'Cushion Covers', 'Kurtas', 'Soup Bowls', 'Plates'],
    datasets: [{
      label: 'Sales of products',
      data: [1210, 1890, 2305, 500, 930, 630, 4350, 3000, 2970, 760, 450, 5450],
      border: 1,
      backgroundColor: [
        'rgba(191, 0, 25, 0.6)', 'rgba(219, 114, 0, 0.6)', 'rgba(239, 183, 0, 0.6)', 'rgba(0, 143, 106, 0.6)', 
        'rgba(0, 100, 176, 0.6)', 'rgba(146, 3, 204, 0.6)', 'rgba(85, 98, 112, 0.6)', 'rgba(244, 143, 177, 0.6)', 
        'rgba(244, 192, 140, 0.6)', 'rgba(244, 226, 137, 0.6)', 'rgba(167, 232, 206, 0.6)', 'rgba(177, 205, 244, 0.6)'
      ],
    }],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    },
    plugins: {
      legend: {
        labels: {
          // increase font size of label
          font: {
            size: 20
          }
        }
      }
    }
  }
});
