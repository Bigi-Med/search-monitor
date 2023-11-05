'use client'
import Image from 'next/image'
import styles from './page.module.css'
import LinkBorder from './components/LinkBorder'
import axios from 'axios'
import {useState} from 'react'

export default function Home() {
  const [showPopup, setShowPopup] = useState<Boolean>(false);
  const [keywords, setKeywords] = useState<Array<String>>([''])
  const [links, setLinks] = useState<Array<String>>([''])
  const [Loading, setLoading] = useState<Boolean>(false)



  const closePopUp = () => {
    setShowPopup(false)
  }

  const parseResponse = (response:any) => {
    let temp_link:Array<String> = []
    let temp_keywords:Array<String> = []

    for (let i = 0; i < response.length; i++) {
      if(response[i]['url'].split('/')[2]=='consent.google.com')
      {
        continue;
      }

      temp_link.push(response[i]['url']);
      temp_keywords.push(response[i]['found'])
    }


    return{
      myKeywords:temp_keywords,
      myLinks:temp_link
    }

  }
  const getAuthGuild = () => {
     setShowPopup(true)
  }

  const getPublisher = async () => {
    setLoading(true)
    const response = await  axios.get('http://localhost:5000/publisher')
     setShowPopup(true)

    let keyword_dict =parseResponse(response.data)
    setLoading(false)
    setKeywords(keyword_dict.myKeywords)
    setLinks(keyword_dict.myLinks)
  }

  const getGuardian = async () => {
    setLoading(true)
    const response = await  axios.get('http://localhost:5000/guardian')
    setShowPopup(true)

    let keyword_dict = parseResponse(response.data)
    setLoading(false)
    setKeywords(keyword_dict.myKeywords)
    setLinks(keyword_dict.myLinks)
  }

  const getGoogle = async (link:string) => {
    setLoading(true)
    
    const response = await axios.get(`http://localhost:5000/google?url=${encodeURIComponent(link)}`);

    
    setShowPopup(true)

    let keyword_dict = parseResponse(response.data)
    setLoading(false)
    setKeywords(keyword_dict.myKeywords)
    setLinks(keyword_dict.myLinks)
  }


  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <div className={styles.leftContainer}>
          {/* <LinkBorder link='https://authorsguild.org/news/?sort=date-DESC' logo='test' onClick={getAuthGuild}>
            </LinkBorder>  */}
          <LinkBorder link='https://www.publishersweekly.com/pw/by-topic/industry-news/index.html' logo='test' onClick={getPublisher}>
          </LinkBorder>
          {showPopup && (
          <div className={styles.popup}>
            {keywords.map((keyword, index) => (
              <div key={index} className={styles.linkKeywords}>
                <br></br>
                <span style={{fontWeight: 'bold', color:'black'}}>Keywords:</span> <span style={{color:'black'}}>{keyword + ' '} </span> <br></br>
                <span style={{fontWeight: 'bold', color:'black'}}>Link: </span> <a style={{color:'blue'}} href={links[index].toString()}>{links[index]}</a>
              </div>
            ))}
          <button className={styles.closeButton} onClick={closePopUp}>Close</button>
          </div>
          
        )}
          {Loading && (
          <div className={styles.loadingDiv}>
          <img src="/assets/Dual-Ring-removebg.png" className={styles.loadingIcon} alt="Loading" />
        </div>
        )}
          <LinkBorder link='https://www.publishersweekly.com/pw/by-topic/industry-news/financial-reporting/index.html' logo='test' onClick={getPublisher}>  
          </LinkBorder>
          <LinkBorder link='https://www.theguardian.com/books' logo='test' onClick={getGuardian}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=amazon kdp&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={() => getGoogle('https://news.google.com/search?q=amazon kdp&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=kindle direct publishing&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={() => getGoogle('https://news.google.com/search?q=kindle direct publishing&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
        
        </div>
        <div className={styles.rightContainer}>
          <LinkBorder link='https://news.google.com/search?q=self publishing&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={() => getGoogle('https://news.google.com/search?q=self publishing&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=ai book lawsuit&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={() => getGoogle('https://news.google.com/search?q=ai book lawsuit&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=ai writing lawsuit&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={() => getGoogle('https://news.google.com/search?q=ai writing lawsuit&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=ai created book&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={() => getGoogle('https://news.google.com/search?q=ai created book&hl=en-US&gl=US&ceid=US%3Aen')}>  
          </LinkBorder>
          <LinkBorder link='https://news.google.com/search?q=author&hl=en-US&gl=US&ceid=US%3Aen' logo='test' onClick={() => getGoogle('https://news.google.com/search?q=author&hl=en-US&gl=US&ceid=US%3Aen')}>
          </LinkBorder>

        
        </div>
      </div>

    </main>
  )
}
