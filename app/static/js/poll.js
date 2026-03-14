(function () {
  const badge = document.getElementById('pending-badge');
  if (!badge) return;

  function fetchCount() {
    fetch('/admin/api/pending-count')
      .then(res => res.json())
      .then(data => {
        badge.textContent = data.count;
        badge.style.display = data.count > 0 ? 'inline' : 'none';
      })
      .catch(() => { badge.textContent = '?'; });
  }

  fetchCount();
  setInterval(fetchCount, 30000);
})();
