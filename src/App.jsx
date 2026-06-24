import { useState, useRef, useEffect, useCallback } from 'react'
import './App.css'

const IMAGES = [
  { id: 1, file: '/images/bandeja_1.jpg', label: 'Bandeja 1' },
  { id: 2, file: '/images/bandeja_2.jpg', label: 'Bandeja 2' },
  { id: 3, file: '/images/bandeja_3.jpg', label: 'Bandeja 3' },
  { id: 4, file: '/images/bandeja_4.jpg', label: 'Bandeja 4' },
  { id: 5, file: '/images/bandeja_5.jpg', label: 'Bandeja 5' },
  { id: 6, file: '/images/bandeja_6.jpg', label: 'Bandeja 6' },
  { id: 7, file: '/images/bandeja_7.jpg', label: 'Bandeja 7' },
  { id: 8, file: '/images/bandeja_8.jpg', label: 'Bandeja 8' },
  { id: 9, file: '/images/bandeja_9.jpg', label: 'Bandeja 9' },
]

function ImageMarker({ image, markers, onAddMarker, onRemoveMarker, isActive, onClick }) {
  const containerRef = useRef(null)
  const imgRef = useRef(null)
  const [scale, setScale] = useState({ x: 1, y: 1 })

  useEffect(() => {
    const updateScale = () => {
      if (imgRef.current && containerRef.current) {
        const naturalW = imgRef.current.naturalWidth
        const naturalH = imgRef.current.naturalHeight
        const displayW = imgRef.current.clientWidth
        const displayH = imgRef.current.clientHeight
        setScale({
          x: naturalW / displayW,
          y: naturalH / displayH,
        })
      }
    }
    updateScale()
    window.addEventListener('resize', updateScale)
    return () => window.removeEventListener('resize', updateScale)
  }, [])

  const handleImageClick = (e) => {
    if (!isActive) {
      onClick()
      return
    }
    const rect = imgRef.current.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top
    onAddMarker(image.id, { x, y })
  }

  const handleMarkerClick = (e, markerId) => {
    e.stopPropagation()
    onRemoveMarker(image.id, markerId)
  }

  return (
    <div
      ref={containerRef}
      className={`image-marker ${isActive ? 'active' : ''}`}
      onClick={handleImageClick}
    >
      <img
        ref={imgRef}
        src={image.file}
        alt={image.label}
        className="bandeja-img"
        onLoad={() => {
          if (imgRef.current) {
            const naturalW = imgRef.current.naturalWidth
            const naturalH = imgRef.current.naturalHeight
            const displayW = imgRef.current.clientWidth
            const displayH = imgRef.current.clientHeight
            setScale({
              x: naturalW / displayW,
              y: naturalH / displayH,
            })
          }
        }}
      />
      {markers.map((m, i) => (
        <div
          key={m.id}
          className="marker"
          style={{ left: m.x - 12, top: m.y - 12 }}
          onClick={(e) => handleMarkerClick(e, m.id)}
          title="Clic para eliminar"
        >
          {i + 1}
        </div>
      ))}
      <div className="marker-count">
        {markers.length} 🐸
      </div>
    </div>
  )
}

function App() {
  const [currentImage, setCurrentImage] = useState(0)
  const [allMarkers, setAllMarkers] = useState({})
  const [history, setHistory] = useState([])

  const markers = allMarkers[currentImage] || []

  const addMarker = useCallback((imgId, pos) => {
    const newMarker = { id: Date.now() + Math.random(), x: pos.x, y: pos.y }
    setAllMarkers(prev => ({
      ...prev,
      [imgId]: [...(prev[imgId] || []), newMarker]
    }))
    setHistory(prev => [...prev, { action: 'add', imgId, marker: newMarker }])
  }, [])

  const removeMarker = useCallback((imgId, markerId) => {
    setAllMarkers(prev => ({
      ...prev,
      [imgId]: (prev[imgId] || []).filter(m => m.id !== markerId)
    }))
    setHistory(prev => [...prev, { action: 'remove', imgId, markerId }])
  }, [])

  const undo = () => {
    if (history.length === 0) return
    const last = history[history.length - 1]
    if (last.action === 'add') {
      setAllMarkers(prev => ({
        ...prev,
        [last.imgId]: (prev[last.imgId] || []).filter(m => m.id !== last.marker.id)
      }))
    } else if (last.action === 'remove') {
      // We don't have the position anymore, so we can't fully restore
      // Just note it
    }
    setHistory(prev => prev.slice(0, -1))
  }

  const clearCurrent = () => {
    setAllMarkers(prev => ({ ...prev, [currentImage]: [] }))
  }

  const clearAll = () => {
    setAllMarkers({})
    setHistory([])
  }

  const totalCount = Object.values(allMarkers).reduce((sum, m) => sum + m.length, 0)

  const exportData = () => {
    const data = IMAGES.map(img => ({
      bandeja: img.label,
      renacuajos: (allMarkers[img.id] || []).length,
      marcas: (allMarkers[img.id] || []).map((m, i) => ({ numero: i + 1, x: Math.round(m.x), y: Math.round(m.y) }))
    }))
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `conteo_renacuajos_${new Date().toISOString().slice(0, 10)}.json`
    a.click()
    URL.revokeObjectURL(url)
  }

  return (
    <div className="app">
      <header className="header">
        <h1>🐸 Contador de Renacuajos</h1>
        <div className="total">
          <span className="total-number">{totalCount}</span>
          <span className="total-label">renacuajos totales</span>
        </div>
      </header>

      <div className="main">
        <div className="sidebar">
          <h2>Bandejas</h2>
          {IMAGES.map((img, idx) => (
            <button
              key={img.id}
              className={`bandeja-btn ${idx === currentImage ? 'active' : ''}`}
              onClick={() => setCurrentImage(idx)}
            >
              <span className="bandeja-name">{img.label}</span>
              <span className="bandeja-count">
                {(allMarkers[idx] || []).length} 🐸
              </span>
            </button>
          ))}

          <div className="sidebar-actions">
            <button onClick={undo} disabled={history.length === 0} className="btn btn-undo">
              ↩ Deshacer
            </button>
            <button onClick={clearCurrent} className="btn btn-clear-current">
              ✕ Limpiar actual
            </button>
            <button onClick={clearAll} className="btn btn-clear-all">
              🗑 Limpiar todo
            </button>
            <button onClick={exportData} className="btn btn-export">
              💾 Exportar JSON
            </button>
          </div>
        </div>

        <div className="viewer">
          <div className="viewer-header">
            <h2>{IMAGES[currentImage].label}</h2>
            <p className="hint">
              {markers.length === 0
                ? 'Haz clic en la imagen para marcar cada renacujo'
                : `${markers.length} renacuajos marcados — clic en un número para quitarlo`}
            </p>
          </div>
          <ImageMarker
            image={IMAGES[currentImage]}
            markers={markers}
            onAddMarker={addMarker}
            onRemoveMarker={removeMarker}
            isActive={true}
            onClick={() => {}}
          />
        </div>
      </div>

      <footer className="footer">
        <div className="summary">
          {IMAGES.map((img, idx) => (
            <span key={img.id} className="summary-item">
              {img.label}: <strong>{(allMarkers[idx] || []).length}</strong>
            </span>
          ))}
        </div>
      </footer>
    </div>
  )
}

export default App
