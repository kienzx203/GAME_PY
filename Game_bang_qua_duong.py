# pygame 10
# Thêm quân thù và làm chúng chạy nhanh hơn

import pygame

# Xác định kích thước màn hình, tiêu đề màn hình
CHIEU_RONG_MAN_HINH = 800
CHIEU_CAO_MAN_HINH = 800
TIEU_DE_MAN_HINH = 'Crossy Game'

# Các màu sắc được xác định bởi hệ màu RGB
MAU_TRANG = (255, 255, 255)
MAU_DEN = (0, 0, 0)

# Thiết lập biến đồng hồ
dong_ho = pygame.time.Clock()



# Định nghĩa lớp trò chơi
class TroChoi:
    toc_do_bam_gio = 60 # tương đương FPS = 60
    # Biến Kiểm tra xem game kết thúc hay chưa
    game_over = False
    
    def __init__(self, duong_dan_hinh_nen, tieu_de, chieu_rong, chieu_cao):
        self.tieu_de = tieu_de
        self.chieu_rong = chieu_rong
        self.chieu_cao = chieu_cao
        
        # Thiết lập biến màn hình với kích thước cho trước
        # và tô màu màn hình, thiết lập tiêu đề màn hình
        self.man_hinh_game = pygame.display.set_mode((chieu_rong, chieu_cao))
        self.man_hinh_game.fill(MAU_TRANG)
        # Load hình nền
        hinh_nen = pygame.image.load(duong_dan_hinh_nen)
        self.hinh_nen = pygame.transform.scale(hinh_nen, (chieu_rong, chieu_cao))
        
    def chay_vong_lap_game(self, he_so_toc_do):
        game_over = False
        chien_thang = False
        chieu = 0
        
        # Tao các đối tượng
        nhan_vat_nguoi_choi = NhanVatNguoiChoi('nhan_vat.png', 375, 700, 50, 50)
        quan_thu_0 = QuanThu('quan_thu.png', 20, 400, 50, 50)
        quan_thu_1 = QuanThu('quan_thu.png', 750, 200, 50, 50)
        quan_thu_2 = QuanThu('quan_thu.png', 750, 600, 50, 50)
        kho_bau = DoiTuongGame('kho_bau.png', 375, 50, 50, 50)
        
        # Tăng tốc độ quân thù theo hệ số
        quan_thu_0.toc_do *= he_so_toc_do
        
        # Vòng lặp game
        while not game_over:
            # Lấy tất cả sự kiện
            for su_kien in pygame.event.get():
                # Nếu sự kiện phát sinh là thoát 
                if su_kien.type == pygame.QUIT:
                    game_over = True
                # Thêm sự kiển nhấn bàn phím, khi người dùng nhấn xuống
                elif su_kien.type == pygame.KEYDOWN:
                    if su_kien.key == pygame.K_UP:
                        chieu = 1
                    elif su_kien.key == pygame.K_DOWN:
                        chieu = -1
                # Sự kiện phát sinh khi người dùng thả phím
                elif su_kien.type == pygame.KEYUP:
                    if su_kien.key == pygame.K_UP or su_kien.key == pygame.K_DOWN:
                        chieu = 0
                # In ra sự kiện phát sinh
                print(su_kien)
            
            
            # Di chuyển
            nhan_vat_nguoi_choi.di_chuyen(chieu, self.chieu_cao)
            quan_thu_0.di_chuyen(self.chieu_rong)
            
            # Tô lại nền cho game
            self.man_hinh_game.fill(MAU_TRANG)
            
            # Vẽ hình nền ra màn hình
            self.man_hinh_game.blit(self.hinh_nen, (0, 0))
            
            # Vẽ các đối tượng lên màn hình
            nhan_vat_nguoi_choi.ve(self.man_hinh_game)
            quan_thu_0.ve(self.man_hinh_game)
            kho_bau.ve(self.man_hinh_game)
            
            # Vẽ các quân thù 1, 2 ra màn hình nếu đạt đến 1 vòng chơi nhất định
            if he_so_toc_do >=2:
                quan_thu_1.di_chuyen(self.chieu_rong)
                quan_thu_1.ve(self.man_hinh_game)
            if he_so_toc_do >=3:
                quan_thu_2.di_chuyen(self.chieu_rong)
                quan_thu_2.ve(self.man_hinh_game)
            
            # Kiểm tra va chạm
            if nhan_vat_nguoi_choi.kiem_tra_va_cham(quan_thu_0):
                game_over = True
                chien_thang = False
                van_ban = font.render('You lost :(', True, MAU_DEN)
                self.man_hinh_game.blit(van_ban, (300, 350))
                pygame.display.update()
                dong_ho.tick(1)
            elif nhan_vat_nguoi_choi.kiem_tra_va_cham(kho_bau):
                game_over = True
                chien_thang = True
                van_ban = font.render('You Won !!', True, MAU_DEN)
                self.man_hinh_game.blit(van_ban, (300, 350))
                pygame.display.update()
                dong_ho.tick(1)
 
            # Cập nhật, thực hiện kết xuất hình ảnh
            pygame.display.update()
            dong_ho.tick(self.toc_do_bam_gio)
            
       
        if chien_thang:
            self.chay_vong_lap_game(he_so_toc_do + 0.5)
        else:
            return

class DoiTuongGame:
    def __init__(self, duong_dan_hinh_anh, x, y, chieu_rong, chieu_cao):
        self.vitri_x = x
        self.vitri_y = y
        self.chieu_rong = chieu_rong
        self.chieu_cao = chieu_cao
        
        # Load hình ảnh vào biến và thay đổi kích thước cho phù hợp
        hinh_doi_tuong = pygame.image.load(duong_dan_hinh_anh)
        self.hinh_anh = pygame.transform.scale(hinh_doi_tuong, (chieu_rong, chieu_cao))
    
    # Phương thức vẽ đối tượng ra màn hình    
    def ve(self, nen):
        nen.blit(self.hinh_anh, (self.vitri_x, self.vitri_y))

class NhanVatNguoiChoi(DoiTuongGame):
    TOC_DO = 10
    
    def __init__(self, duong_dan_hinh_anh, x, y, chieu_rong, chieu_cao):
        super().__init__(duong_dan_hinh_anh, x, y, chieu_rong, chieu_cao)
      
    def di_chuyen(self, chieu, chieu_cao_man_hinh):
        # Chiều > 0 => nhân vật đi lên, <0 nhân vật đi xuống
        if chieu > 0:
            self.vitri_y -= self.TOC_DO
        elif chieu < 0:
            self.vitri_y += self.TOC_DO
            
        if self.vitri_y >= chieu_cao_man_hinh - 70:
            self.vitri_y = chieu_cao_man_hinh - 70
            
    
    def kiem_tra_va_cham(self, doi_tuong_khac):
        if self.vitri_y > doi_tuong_khac.vitri_y + doi_tuong_khac.chieu_cao:
            return False
        elif self.vitri_y + self.chieu_cao < doi_tuong_khac.vitri_y:
            return False
        
        if self.vitri_x > doi_tuong_khac.vitri_x + doi_tuong_khac.chieu_rong:
            return False
        elif self.vitri_x + self.chieu_rong < doi_tuong_khac.vitri_x:
            return False
        
        return True
        
class QuanThu(DoiTuongGame):
    toc_do = 10
    
    def __init__(self, duong_dan_hinh_anh, x, y, chieu_rong, chieu_cao):
        super().__init__(duong_dan_hinh_anh, x, y, chieu_rong, chieu_cao)

            
    def di_chuyen(self, chieu_rong_man_hinh):
        if self.vitri_x <= 20:
            self.toc_do = abs(self.toc_do)
        elif self.vitri_x >= chieu_rong_man_hinh - 70:
            self.toc_do = -abs(self.toc_do)
 
        self.vitri_x += self.toc_do
            
pygame.init()

pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

tro_choi = TroChoi('hinh_nen.png', TIEU_DE_MAN_HINH, CHIEU_RONG_MAN_HINH, CHIEU_CAO_MAN_HINH)
tro_choi.chay_vong_lap_game(1)

pygame.quit()
quit()









