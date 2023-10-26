'use client'
import Image from 'next/image'
import styles from './page.module.css'
import LinkBorder from './components/LinkBorder'
import axios from 'axios'

export default function Home() {

  const getAuthGuild = () => {
    console.log("https://authorsguild.org/news/?sort=date-DESC")
  }

  const getPublisher = async () => {
    const response = await  axios.get('http://localhost:5000/publisher')

    console.log(response)
  }

  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <div className={styles.leftContainer}>
          <LinkBorder link='https://authorsguild.org/news/?sort=date-DESC' logo='test' onClick={getAuthGuild}>
            </LinkBorder> 
          <LinkBorder link='https://www.publishersweekly.com/pw/by-topic/industry-news/index.html' logo='test' onClick={getPublisher}>
          </LinkBorder>
          <LinkBorder link='https://www.publishersweekly.com/pw/by-topic/industry-news/financial-reporting/index.html' logo='test' onClick={getPublisher}>  
          </LinkBorder>
          <LinkBorder link='https://www.theguardian.com/books' logo='test' onClick={getAuthGuild}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=amazon kdp&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={getAuthGuild}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=kindle direct publishing&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={getAuthGuild}>  
          </LinkBorder>
        
        </div>
        <div className={styles.rightContainer}>
          <LinkBorder link='https://news.google.com/search?q=self publishing&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={getAuthGuild}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=ai book lawsuit&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={getAuthGuild}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=ai writing lawsuit&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={getAuthGuild}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=ai created book&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={getAuthGuild}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=author&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={getAuthGuild}>
          </LinkBorder>

        
        </div>
      </div>

    </main>
  )
}
