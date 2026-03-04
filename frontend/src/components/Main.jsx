import React from 'react'
import S from '../style/Main.module.css'
import Post from './Post'
import Sidebar from './Sidebar'
import Header from './Header'

export default function Main() {
  return (
    <div>
        <Header/>
        <div className={S.main_container}>
            <Sidebar/>
            <main className={S.content}>
                <Post/>
                <Post/>
                <Post/>
            </main>
        </div>
    </div>
  )
}
