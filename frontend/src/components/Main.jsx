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
            <div className={S.content}>
                <h2 className={S.section_title}>Статьи</h2>
                <div className={S.posts_list}>
                    <Post />
                    <Post />
                    <Post />
                </div>
            </div>
        </div>
    </div>
  )
}
