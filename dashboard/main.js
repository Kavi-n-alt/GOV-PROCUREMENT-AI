const apiBase = "/api";

async function fetchTenders() {
  const res = await fetch(`${apiBase}/tenders`);
  const items = await res.json();
  const container = document.getElementById("tenders");
  if (!items || items.length === 0) {
    container.innerHTML = '<p>No tenders found.</p>';
    return;
  }

  container.innerHTML = "";
  const list = document.createElement("ul");
  items.forEach(t => {
    const li = document.createElement("li");
    li.innerHTML = `<strong>${escapeHtml(t.title)}</strong> - <small>${t.created_at || ''}</small><p>${escapeHtml(t.description || '')}</p>`;
    list.appendChild(li);
  });
  container.appendChild(list);
}

function escapeHtml(unsafe) {
  return (unsafe || '').replace(/[&<"'>]/g, function(m) { return ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":"&#039;"})[m]; });
}

async function handleUpload(e) {
  e.preventDefault();
  const status = document.getElementById('upload-status');
  const form = e.target;
  const fileInput = document.getElementById('file');
  if (!fileInput.files || !fileInput.files[0]) {
    status.textContent = 'Please select a file.';
    return;
  }
  status.textContent = 'Uploading...';

  const formData = new FormData();
  formData.append('file', fileInput.files[0]);

  try {
    const res = await fetch(`${apiBase}/upload`, { method: 'POST', body: formData });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Upload failed');
    status.textContent = `Upload accepted (id: ${data.tender_id || 'n/a'})`;
    fileInput.value = '';
    fetchTenders();
  } catch (err) {
    status.textContent = `Error: ${err.message}`;
  }
}

document.getElementById('upload-form').addEventListener('submit', handleUpload);
window.addEventListener('load', () => {
  fetchTenders();
});